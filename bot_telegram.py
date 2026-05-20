import os
import asyncio
import sys
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# ============================================================================
# 1. CONFIGURAZIONE DEL TOKEN
# ============================================================================
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("❌ ERRORE CRITICO: Variabile TELEGRAM_BOT_TOKEN non trovata.")
    print("   Assicurati di averla impostata su Render (Environment Variables).")
    sys.exit(1) # Esce dal programma se il token non c'è

# ============================================================================
# 2. COMANDI DEL BOT (LOGICA)
# ============================================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Risponde al comando /start."""
    await update.message.reply_text('🎬 Ciao! Il bot è online! Usa /video1 per un test.')

async def video1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Risponde al comando /video1."""
    await update.message.reply_text("✅ Video 1 (presto disponibile con il link da Drive).")

# ============================================================================
# 3. AVVIO DEL BOT (MODIFICATO PER RENDER)
# ============================================================================
async def main():
    # Crea l'applicazione
    app = Application.builder().token(TOKEN).build()
    
    # Aggiunge i gestori dei comandi
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("video1", video1))
    
    # Avvia il bot (questo è il modo corretto per le nuove versioni)
    print("🤖 Bot avviato con successo! In ascolto...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # Mantiene il bot in esecuzione (aspetta che venga fermato)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
