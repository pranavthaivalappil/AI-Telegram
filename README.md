# 🤖 AI Telegram Image Classifier Bot

A powerful Telegram bot that uses AI (ResNet50 neural network) to classify and analyze images sent by users.

## 🚀 Quick Start Guide

### Step 1: Get a Telegram Bot Token
1. Open Telegram and search for `@BotFather`
2. Start a chat with BotFather
3. Send `/newbot`
4. Choose a name for your bot (e.g., "My Image Classifier Bot")
5. Choose a username ending with 'bot' (e.g., "myimageclassifier_bot")
6. **Copy the token** BotFather gives you (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Install Python 3.12
1. **Download Python 3.12** from: https://www.python.org/downloads/release/python-31212/
2. Download "Windows installer (64-bit)" (`python-3.12.12-amd64.exe`)
3. **Important**: Check "Add Python to PATH" during installation
4. Choose "Install for all users" if prompted

### Step 3: Set Up the Environment
1. **Double-click** `setup_python312.bat`
2. Wait for the setup to complete (this will install TensorFlow and all dependencies)

### Step 4: Configure Your Bot Token
1. **Run**: `set_token.bat YOUR_BOT_TOKEN_HERE`
   - Example: `set_token.bat 123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 5: Start Your Bot
1. **Double-click** `run_bot.bat`
2. Wait for "✅ Bot ready!" message
3. **Test it**: Send a photo to your bot on Telegram!

## 📱 How to Use

1. **Find your bot** on Telegram using the username you created
2. **Send `/start`** to see the welcome message
3. **Send any photo** and get AI analysis in seconds!
4. **Commands available**:
   - `/start` - Welcome message
   - `/help` - Usage instructions

## 🔧 Features

- 🧠 **AI-Powered**: Uses ResNet50 neural network trained on ImageNet
- 🎯 **Accurate**: Recognizes 1000+ different object categories  
- ⚡ **Fast**: Analysis usually takes 2-5 seconds
- 📊 **Detailed**: Shows top 5 predictions with confidence scores
- 📏 **Image Info**: Displays file size, dimensions, and format
- 🛡️ **Secure**: Token stored in environment variables

## 📁 File Structure

```
├── main.py              # Basic version (Python 3.13 compatible)
├── main_ai.py           # Full AI version (needs Python 3.12)
├── setup_python312.bat  # Automated setup script
├── set_token.bat        # Token configuration script  
├── run_bot.bat          # Bot launcher script
├── requirements.txt     # Dependencies list
└── README.md           # This file
```

## 🐛 Troubleshooting

### "Python 3.12 not found"
- Make sure you installed Python 3.12 and checked "Add to PATH"
- Restart your computer after installation

### "Virtual environment not found"
- Run `setup_python312.bat` first
- Make sure it completed without errors

### "Bot token not found"
- Run `set_token.bat YOUR_TOKEN` with your actual token
- Check that a `.env` file was created

### Bot doesn't respond
- Check that the bot token is correct
- Make sure you started a chat with your bot first
- Verify the bot is running (should show "✅ Bot ready!")

## 🔒 Security Notes

- Your bot token is stored in `.env` file (don't share this file!)
- For production use, consider additional security measures
- The bot only processes images you send to it

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Make sure all steps were followed in order
3. Verify Python 3.12 is properly installed

---
**Enjoy your AI-powered Telegram bot! 🎉** 