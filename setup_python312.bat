@echo off
echo 🚀 Setting up Python 3.12 environment for AI Telegram Bot...
echo.

REM Check if Python 3.12 is installed
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 3.12 not found! Please install Python 3.12 first.
    echo Download from: https://www.python.org/downloads/release/python-31212/
    pause
    exit /b 1
)

echo ✅ Python 3.12 found!
py -3.12 --version

REM Remove old virtual environment if it exists
if exist "venv312" (
    echo 🗑️ Removing old virtual environment...
    rmdir /s /q venv312
)

REM Create new virtual environment with Python 3.12
echo 🔧 Creating virtual environment with Python 3.12...
py -3.12 -m venv venv312

REM Activate virtual environment and install packages
echo 📦 Installing packages...
call venv312\Scripts\activate.bat
python -m pip install --upgrade pip
pip install tensorflow==2.15.0 python-telegram-bot Pillow requests numpy flask

echo.
echo ✅ Setup complete! 
echo.
echo 📝 Next steps:
echo 1. Get your bot token from @BotFather on Telegram
echo 2. Run: set_token.bat YOUR_BOT_TOKEN
echo 3. Run: run_bot.bat
echo.
pause 