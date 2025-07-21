@echo off
echo 🤖 Starting AI Telegram Bot...

REM Check if virtual environment exists
if not exist "venv312" (
    echo ❌ Virtual environment not found!
    echo Please run setup_python312.bat first
    pause
    exit /b 1
)

REM Check if token is set
if not exist ".env" (
    echo ❌ Bot token not found!
    echo Please run: set_token.bat YOUR_BOT_TOKEN
    pause
    exit /b 1
)

REM Load environment variables
for /f "tokens=1,2 delims==" %%a in (.env) do set %%a=%%b

REM Activate virtual environment and run bot
call venv312\Scripts\activate.bat
echo 🚀 Starting bot with AI image classification...
python main_ai.py

pause 