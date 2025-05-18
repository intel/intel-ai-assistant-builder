# Go Client for Intel® AI Assistant Builder Service
This folder contains a simple Go client designed to communicate with Intel® AI Assistant Builder Service.

## Install Dependencies
- Please ensure that **[Go](https://go.dev/dl/)** is installed on your system. Then, navigate to the `example\golang` directory and download the  necessary modules:
```
cd example\golang
go mod download
```

## How to Run
- Before executing the Go Client, please ensure that Intel® AI Assistant Builder Service is already running.
```
cd example\golang
go run .
```

## Recompile Proto to pb.go
- Use the Powershell script `shared\recompile-client-proto.ps1` to regenerate the `pb`/`pb2` files for Golang.
```
cd path\to\shared
.\recompile-client-proto.ps1
```
