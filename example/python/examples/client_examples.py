import os
import sys
SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(SCRIPT_DIR,'..')))
import helpers.chat as chat
import helpers.parameters as param
import helpers.config as config
import helpers.model as model

def switch_model(stub):
    model_name = None
    model_link = None
    db_config = config.get_config(stub)
    all_models = db_config["ActiveAssistant"]["all_models"]
    active_models = {}
    for active in db_config["ActiveAssistant"]["models"]:
        if active["model_type"] == "chat_model":
            active_models = active
            break
    for index, model_option in enumerate(all_models):
        if model_option["full_name"] == active_models["full_name"]:
            print(f"{index}. Model: {model_option["full_name"]} (Active)")
        else:
            print(f"{index}. Model: {model_option["full_name"]}")
    selected = input("Select the model to switch to: ")
    if int(selected) >= 0 and int(selected) < len(all_models):
        if all_models[int(selected)]["full_name"] == active_models["full_name"]:
            print("Model is already active.")
            return
        model_name = all_models[int(selected)]["full_name"]
        model_link = all_models[int(selected)]["download_link"]
    if model_name is None and model_link is None:
        print("Invalid selection.")
        return
    full_path = os.path.join(db_config["local_model_hub"], model_name)
    if not os.path.exists(full_path):
        print(f"Local folder for model '{model_name}' does not exist.  Downloading...")
        try:
            model.download(stub, model_link, db_config["local_model_hub"])
        except Exception as e:
            print(f"Error downloading model: {e}")
    else:
        print(f"Model '{model_name}' already exists. Switching...")
    # response = model.switch(stub, db_config["local_model_hub"], model_name)
    # return response