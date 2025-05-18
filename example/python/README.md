# Python Client for Intel® AI Assistant Builder Service
This folder contains a simple Python client designed to communicate with Intel® AI Assistant Builder Service.

## Install Dependencies
- Download and install **[Python 3.12.9](https://www.python.org/downloads/release/python-3129/)**.
- Use the script `example\python\install.bat` to install necessary dependencies.
```
cd path\to\example\python
install.bat
```

## How to Run 
- Execute the script `example\python\run.bat` to start the example.
```
cd path\to\example\python
run.bat
```

- Execute the script `example\python\run_tests.bat` to perform tests.
```
cd path\to\example\python
run_tests.bat
```

## Generate Python Proto File
- Use the PowerShell script `shared\recompile-client-proto.ps1` to regenerate the `pb`/`pb2` files for Python.
```
cd path\to\shared
.\recompile-client-proto.ps1
```
