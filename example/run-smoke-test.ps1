#Requires -RunAsAdministrator
if (-not [Environment]::GetEnvironmentVariable('PROTOC'))
{
    "Environment PROTOC is not configured"
    "check scripts/README.md on how to fix this"
    exit 1
}

$root_dir="$PSScriptRoot\\.." | Resolve-Path

try { Get-Process -Id (Get-NetTCPConnection -LocalPort 5006).OwningProcess }
catch { "Superbuilder service is not running on port 5006. Force quit"; exit 1 }

"Superbuilder service is running. continue with the smoke test"
""
""
"regenerate proto before running smoke test"
"========================================="
cd $root_dir\\shared
./recompile-client-proto.ps1
cd $PSScriptRoot # return to script's directory
""
""
"running python client"
"====================="
cd $root_dir\\example\\python
./install.bat
./run_tests.bat
$python_unit_test_exit_code=$?

cd $PSScriptRoot # return to script's directory
""
""
"running go client"
"================="
cd $root_dir\\example\\golang
go mod download
go run .
$go_client_exit_code = $?
cd $PSScriptRoot # return to script's directory
""
""
"running csharp client"
"================="
cd $root_dir\\example\\csharp\\CSharpClientExample
dotnet restore
dotnet build
dotnet run
$csharp_client_exit_code = $?
cd $PSScriptRoot # return to script's directory


"Python client exit gracefully: $python_unit_test_exit_code"
"Go client exit gracefully: $go_client_exit_code"
"C# client exit gracefully: $csharp_client_exit_code"
if (-not $python_unit_test_exit_code) {
    throw "Python client tests failed with exit code $python_unit_test_exit_code"
}

if (-not $go_client_exit_code) {
    throw "Go client tests failed with exit code $go_client_exit_code"
}

if (-not $csharp_client_exit_code) {
    throw "C# client tests failed with exit code $csharp_client_exit_code"
}
