import os
import io
import numpy as np
import requests
from flask import Flask, request, jsonify
from PIL import Image
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)

# Use environment variable for bot token (more secure)
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '6878977223:AAFiJL6niL4eLMrsjclq__BbGOAVw6Mnn5w')

async def classify_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle image classification requests"""
    if not update.message:
        return
        
    if update.message.photo:
        # Get the largest photo size
        file_id = update.message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        
        if not file.file_path:
            await update.message.reply_text("Sorry, couldn't access the image file.")
            return
        
        # Download and process the image
        img_data = requests.get(file.file_path).content
        img = Image.open(io.BytesIO(img_data))
        
        # Get image properties
        width, height = img.size
        format_name = img.format or "Unknown"
        mode = img.mode
        
        # For now, provide image analysis instead of AI classification
        # TODO: Replace with actual AI model when TensorFlow supports Python 3.13
        result = {
            'status': 'Image received and analyzed',
            'properties': {
                'width': width,
                'height': height,
                'format': format_name,
                'mode': mode,
                'size_kb': len(img_data) // 1024
            },
            'note': 'AI classification will be available when TensorFlow supports Python 3.13+'
        }
        
        response = f"📸 Image Analysis:\n"
        response += f"• Size: {width}x{height} pixels\n"
        response += f"• Format: {format_name}\n"
        response += f"• File size: {len(img_data) // 1024} KB\n"
        response += f"• Color mode: {mode}\n\n"
        response += f"🤖 AI classification coming soon when TensorFlow supports Python 3.13!"
        
        await update.message.reply_text(response)
    else:
        await update.message.reply_text('Please send a photo for analysis! 📷')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    if not update.message:
        return
        
    welcome_message = (
        "🤖 Welcome to the Image Analysis Bot!\n\n"
        "Send me any photo and I'll analyze it for you.\n"
        "Currently providing basic image analysis.\n"
        "AI classification will be added when TensorFlow supports Python 3.13+\n\n"
        "Just send a photo to get started! 📸"
    )
    await update.message.reply_text(welcome_message)

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.PHOTO, classify_image))
    
    # Start the bot
    print("🚀 Bot is starting...")
    print("Send /start to begin or just send a photo!")
    print("Press Ctrl+C to stop")
    
    application.run_polling()

if __name__ == '__main__':
    main()