# Intel® AI Assistant Builder Service Client Examples

<p align="justify">This folder contains sample code for a <strong>terminal-based client</strong> for Intel® AI Assistant Builder. We believe this will assist developers in quickly prototyping new features and integrations with Intel® AI Assistant Builder Service.</p>

- **[Prerequisites](#prerequisites)**
- **[GRPC Dependency](#grpc-dependency)**
- **[Smoke Test](#smoke-test)**
- **Client Examples**
    - [C# Client Example](csharp/CSharpClientExample/README.md)
    - [Python Client Example](python/README.md)
    - [Golang Client Example](golang/README.md)
***

### Prerequisites
<details open>
<summary><strong>1. Protoc</strong></summary>

>* Protoc is **essential for the C#, Python, Go Client Examples**. Intel® AI Assistant Builder utilizes Protoc to generate `pb`/`pb2` files for **Golang** and **Python**.
>*  **Installation Steps:**
>    1. Download [`protoc-27.2-win64.zip`](https://github.com/protocolbuffers/protobuf/releases/tag/v27.2) file and extract it to the desired location on your computer.
>    2. Set an environment variable named `PROTOC` with the value `\path\to\protoc-27.2-win64\bin\protoc.exe` on your Windows system.
>    3. Open PowerShell and run `$env:PROTOC` to ensure the path is correctly set.
     ![Protoc](../media/protoc.png)
</details>

<details>
<summary><strong>2. Python 3.12.9</strong></summary>
  
>* Python is **essential for Python Client Example**.
>*  **Installation Steps:**
>    1. Download [`Python 3.12.9`](https://www.python.org/downloads/release/python-3129/) and run the installer on your computer.
>    2. Proceed through the installation by following the prompts provided by the installer.
>    3. Once the installation is complete, open Command Prompt and run `python --version` to confirm the installation.
</details>

<details>
<summary><strong>3. Visual Studio 2022 Community</strong></summary>
  
>* Visual Studio 2022 Community is **essential for CSharp Client Example**.
>*  **Installation Steps:**
>    1. Download [`Visual Studio 2022 Community`](https://visualstudio.microsoft.com/vs/) installer.
>    2. Run the installer and select the components for `Desktop Development with C++` and `.NET Desktop Development`.
</details>

<details>
<summary><strong>4. Golang</strong></summary>
  
>* Golang is **essential for Golang Client Example**.
>*  **Installation Steps:**
>    1. Download [`Golang`](https://go.dev/dl/) installer. **Note**: `Go 1.24.1` has been tested for compatibility.
>    2. Run the installer and follow the prompts to complete the installation.
</details>

***

### GRPC Dependency

Intel® AI Assistant Builder uses GRPC for communication with its services.

:information_source: **Service information:**
- Intel® AI Assistant Builder Service runs on `localhost:5006`.
- Intel® AI Assistant Builder Service is named `IntelAiaService.exe`.
- Intel® AI Assistant Builder Service is registered as a Microsoft Windows service. 
- All available services are defined in `shared\superbuilder_middleware.proto`.
- Use the Powershell script `shared\recompile-client-proto.ps1` to regenerate the `pb`/`pb2` files for Golang and Python. 
- C# automatically regenerates its `pb`/`pb2` files each time the code is built.

***

### Smoke Test

Use the file `example\run-smoke-test.ps1` to verify your computer's configuration. By default, this script will run all client tests.
