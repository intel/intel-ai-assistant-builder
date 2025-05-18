@echo off

REM Check if the specified Python executable exists
set python="C:\Program Files\Python312\python.exe"
if not exist %python% (
    echo Specified Python executable not found. Using default location.
    set python="%LocalAppData%\Programs\Python\Python312\python.exe"
)

REM Check if the fallback Python executable exists
if not exist %python% (
    echo Python executable not found in both locations. Exiting.
    exit /b 1
)

echo ===== Creating virtual environment... =====
%python% -m venv .venv

echo ===== Activating virtual environment... =====
call .venv\Scripts\activate

echo ===== Installing packages... =====
pip install -r requirements.txt

echo ===== Deactivating virtual env... =====
call deactivate

exit /b