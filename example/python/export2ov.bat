@echo off
if "%1"=="" (
  echo No first argument provided.
  goto :eof
) else (
    set "mpath=%1"
    @REM Remove trailing backslash if present
    if "%mpath:~-1%"=="\" (
    set "mpath=%mpath:~0,-1%"
    )
    set "opath=%mpath%-ov-int4"
    echo %mpath% - %opath%

    @echo on
    optimum-cli export openvino --model %mpath% --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.8 --sym --trust-remote-code %opath%
)

:eof