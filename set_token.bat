@echo off
if "%1"=="" (
    echo ❌ Please provide your bot token as an argument
    echo Usage: set_token.bat YOUR_BOT_TOKEN
    echo Example: set_token.bat 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
    pause
    exit /b 1
)

echo 🔐 Setting bot token...
echo TELEGRAM_BOT_TOKEN=%1 > .env

echo ✅ Bot token set successfully!
echo ✅ Token saved to .env file
echo.
echo 🚀 Now you can run: run_bot.bat
pause 