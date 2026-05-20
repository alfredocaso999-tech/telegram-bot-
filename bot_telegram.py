import os
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import asyncio

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Token non trovato!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎬 Ciao! Bot funzionante!')

async def video1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Video 1 (presto disponibile)")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("video1", video1))

print("🤖 Bot avviato!")
asyncio.run(app.run_polling())