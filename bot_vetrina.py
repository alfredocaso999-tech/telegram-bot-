import os
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import asyncio

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Token non trovato! Aggiungi la variabile TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎬 Ciao! Video disponibili:\n/video1 - Video 1\n/video3 - Video 3\n/video7 - Video 7')

async def video1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Video 1 (presto disponibile)")

async def video3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Video 3 (presto disponibile)")

async def video7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Video 7 (presto disponibile)")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("video1", video1))
app.add_handler(CommandHandler("video3", video3))
app.add_handler(CommandHandler("video7", video7))

print("🤖 Bot avviato! Resta in ascolto...")

# ⚡ LA RIGA MAGICA PER RENDER ⚡
asyncio.run(app.run_polling())
