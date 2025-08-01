// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
mod grpc_client;
use grpc_client::{SharedClient, super_builder};
use grpc_client::{initialize_client,
    call_chat,connect_client,get_config, mw_say_hello, llm_health_check, remove_file,
    upload_file, send_feedback, download_file, get_file_list, pyllm_say_hello, stop_chat, stop_upload_file, set_assistant_view_model,
    update_notification, get_chat_history, remove_session, send_email, set_models, update_db_models, set_parameters, 
    load_models, upload_model, set_session_name,set_user_config_view_model, convert_model, export_user_config, import_user_config};
//use reqwest::Client;
use tauri::{AppHandle, Manager};
//use tokio::fs::File;
//use tokio::io::AsyncWriteExt;
mod config;
mod status;
use std::env;
use std::fs;
use std::path::Path;
use serde::Serialize;
use std::process::Command;
use base64::{engine::general_purpose::STANDARD, Engine as _};
use image::imageops::FilterType;
use image::ImageReader as ImageReader;
use std::io::Cursor;
use image::GenericImageView;

#[derive(Serialize)]
struct MissingModelsResponse {
    missing_models: Vec<String>,
    models_dir_path: String,
}

#[tauri::command]
fn get_system_language() -> String {
    use sys_locale::get_locale;
    
    get_locale().unwrap_or_else(|| String::from("en"))
}

#[tauri::command]
async fn get_missing_models(
    models_abs_path: String,
    models: Vec<String>,
) -> Result<MissingModelsResponse, String> {
    // Get the current executable path

    // Ensure the models directory exists
    let models_dir_path = Path::new(&models_abs_path);

    if !models_dir_path.exists() {
        println!("Models directory does not exist, creating...");
        fs::create_dir_all(&models_dir_path).map_err(|e| e.to_string())?;
    } else {
        println!("Models directory already exists.");
    }


    // List the files in the models directory
    let mut files_in_directory = Vec::new();
    if let Ok(entries) = fs::read_dir(&models_dir_path) {
        for entry in entries.flatten() {
            if let Ok(file_name) = entry.file_name().into_string() {
                files_in_directory.push(file_name);
            }
        }
    }
    println!("Files in directory: {:?}", files_in_directory);

    // Determine which models are missing
    let missing_models = models
        .into_iter()
        .filter(|model| !files_in_directory.contains(model))
        .collect::<Vec<_>>();

    println!("Missing models: {:?}", missing_models);

    let response = MissingModelsResponse {
        missing_models,
        models_dir_path: format!("{}", models_dir_path.display()),
    };

    Ok(response)
}

#[tauri::command]
fn check_openvino_model(folder_path: String) -> bool {
    let folder_path = Path::new(&folder_path);
    let file1_path = folder_path.join("openvino_model.bin");
    let file2_path = folder_path.join("openvino_model.xml");

    file1_path.exists() && file2_path.exists()
}

fn set_window_borders(window: tauri::WebviewWindow) -> Result<(), String> {
    match window.hwnd() {
    #[cfg(target_os = "windows")]
    Ok(hwnd) => {
        use windows::Win32::{
            Graphics::Dwm::DwmExtendFrameIntoClientArea,
            UI::Controls::MARGINS,
            Foundation::HWND,
        };

        let margins = MARGINS {
            cxLeftWidth: 1,
            cxRightWidth: 1,
            cyTopHeight: 1,
            cyBottomHeight: 1,
        };
        
        unsafe {
            DwmExtendFrameIntoClientArea(HWND(hwnd.0 as isize), &margins).map_err(|err | format!("Error: {:?}", err))
        }
    }
    _ => Err("Unsupported platform".to_string()),
    }
}

#[tauri::command]
async fn set_window_borders_command(app: tauri::AppHandle, window_label: String) -> Result<(), String> {
    if let Some(window) = app.get_webview_window(&window_label) {
        set_window_borders(window)
    } else {
        Err("Window not found".to_string())
    }
}

async fn send_exit(app: &AppHandle) {
    let state = app.state::<SharedClient>();
    let mut client_guard = state.lock().await;
    let client = client_guard.as_mut().unwrap();
    client
        .client_disconnected(super_builder::ClientDisconnectedRequest {})
        .await
        .unwrap();
}

#[tauri::command]
async fn get_schema() -> Result<String, String> {
    let schema = include_str!(concat!(env!("OUT_DIR"), "/schema.json"));
    Ok(schema.to_string())
}

#[tauri::command]
fn open_in_explorer(path: &str) -> Result<(), String> {
    Command::new("explorer")
        .arg(path)
        .spawn()
        .map_err(|e| format!("Failed to open path in Explorer: {}", e))?;
    Ok(())
}

#[tauri::command]
fn open_file_and_return_as_base64(
    filename: String
) -> Result<String, String> {
    
    let path = Path::new(&filename);
    let display = path.display();
    let file = match fs::read(path) {
        Ok(file) => file,
        Err(why) => panic!("couldn't open {}: {}", display, why),
    };

    // Load the image from the file
    let img = ImageReader::new(Cursor::new(file))
        .with_guessed_format()
        .map_err(|e| format!("Failed to read image: {}", e))?
        .decode()
        .map_err(|e| format!("Failed to decode image: {}", e))?;

    let max_width = 40;
    let max_height = 40;
    // Check the image dimensions
    let (width, height) = img.dimensions();
    let resized_img = if width > max_width || height > max_height {
        println!("Resizing image to fit within {w}x{h} while preserving aspect ratio", w=max_width, h=max_height);
    
        // Calculate scaling factor
        let scale = (max_width as f32) / width.max(height) as f32;
    
        // Calculate new dimensions
        let new_width = (width as f32 * scale).round() as u32;
        let new_height = (height as f32 * scale).round() as u32;
    
        // Resize the image while keeping aspect ratio
        img.resize(new_width, new_height, FilterType::Lanczos3)
    } else {
        // Use the original image if it's already small enough
        img
    };

    // Encode the resized image to base64
    let mut buf = Vec::new();
    let mut cursor = Cursor::new(&mut buf);
    resized_img
        .write_to(&mut cursor, image::ImageFormat::from_extension("png").unwrap())
        .map_err(|e| format!("Failed to write image to buffer: {}", e))?;
    let base64 = STANDARD.encode(buf);

    Ok(base64)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
#[tokio::main]
pub async fn run() {
    let client = initialize_client().await;

    let app = tauri::Builder::default()
        .plugin(tauri_plugin_clipboard_manager::init())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_opener::init())
        .setup(|app| {
            let window = app.get_webview_window("main").unwrap();
            set_window_borders(window).unwrap();
            Ok(())
        })
        .manage(client)
        .invoke_handler(tauri::generate_handler![
            get_system_language, call_chat, check_openvino_model,
            connect_client, get_config, remove_file,
            mw_say_hello, download_file, llm_health_check, upload_file,
            send_feedback, get_missing_models, get_file_list, pyllm_say_hello, 
            stop_chat, stop_upload_file, update_notification, set_window_borders_command, open_in_explorer, set_assistant_view_model,            
            get_chat_history, remove_session, send_email, set_models, update_db_models, set_parameters, 
            load_models,convert_model,upload_model,set_session_name, open_file_and_return_as_base64,set_user_config_view_model,get_schema, import_user_config, export_user_config
        ])
        .build(tauri::generate_context!())
        .expect("error while running tauri application");

    app.run(|app, event| match event {
        tauri::RunEvent::ExitRequested { .. } => {
            futures::executor::block_on(send_exit(app));
        }
        _ => {}
    });
}

