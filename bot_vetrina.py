cat > bot_telegram.py << 'EOF'
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8262179130:AAHo_sN4IjhZzYcl9VwsPjafGqv32NgzWrI"

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📦 Prodotti", callback_data='prodotti')],
        [InlineKeyboardButton("📞 Contattaci", callback_data='contatti')],
        [InlineKeyboardButton("ℹ️ Info", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎬 *BENVENUTO NEL MIO SHOWROOM VIDEO* 🎬\n\nSfoglia i miei video e contattami!\n\nClicca sui pulsanti:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def prodotti(update, context):
    keyboard = [
        [InlineKeyboardButton("🎥 Video 1", callback_data='video_1')],
        [InlineKeyboardButton("🎥 Video 3", callback_data='video_3')],
        [InlineKeyboardButton("🎥 Video 7", callback_data='video_7')],
        [InlineKeyboardButton("🎥 Video 8", callback_data='video_8')],
        [InlineKeyboardButton("🎥 Video 9", callback_data='video_9')],
        [InlineKeyboardButton("🎥 Video 10", callback_data='video_10')],
        [InlineKeyboardButton("🔙 Indietro", callback_data='indietro')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("📦 *SELEZIONA UN VIDEO:*", reply_markup=reply_markup, parse_mode='Markdown')

async def invia_video(update, context, video_name, titolo):
    query = update.callback_query
    await query.answer()
    with open(f"{video_name}.mp4", 'rb') as f:
        await context.bot.send_video(update.effective_chat.id, video=f, caption=f"🎥 *{titolo}*", parse_mode='Markdown')

async def video_1(update, context): await invia_video(update, context, "1", "Video 1")
async def video_3(update, context): await invia_video(update, context, "3", "Video 3")
async def video_7(update, context): await invia_video(update, context, "7", "Video 7")
async def video_8(update, context): await invia_video(update, context, "8", "Video 8")
async def video_9(update, context): await invia_video(update, context, "9", "Video 9")
async def video_10(update, context): await invia_video(update, context, "10", "Video 10")

async def contatti(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("🔙 Indietro", callback_data='indietro')]]
    await query.edit_message_text(
        "📞 *CONTATTI*\n\n📱 Telefono: +39 333 1234567\n✉️ Email: info@showroom.it\n💬 Telegram: @tuo_username",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def info(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("🔙 Indietro", callback_data='indietro')]]
    await query.edit_message_text(
        "ℹ️ *INFO*\n\nShowroom video prodotti di alta qualità.\nUsa Prodotti per vedere i video!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def indietro(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📦 Prodotti", callback_data='prodotti')],
        [InlineKeyboardButton("📞 Contattaci", callback_data='contatti')],
        [InlineKeyboardButton("ℹ️ Info", callback_data='info')]
    ]
    await query.edit_message_text(
        "🎬 *MENU PRINCIPALE*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(prodotti, pattern='^prodotti$'))
app.add_handler(CallbackQueryHandler(contatti, pattern='^contatti$'))
app.add_handler(CallbackQueryHandler(info, pattern='^info$'))
app.add_handler(CallbackQueryHandler(indietro, pattern='^indietro$'))
app.add_handler(CallbackQueryHandler(video_1, pattern='^video_1$'))
app.add_handler(CallbackQueryHandler(video_3, pattern='^video_3$'))
app.add_handler(CallbackQueryHandler(video_7, pattern='^video_7$'))
app.add_handler(CallbackQueryHandler(video_8, pattern='^video_8$'))
app.add_handler(CallbackQueryHandler(video_9, pattern='^video_9$'))
app.add_handler(CallbackQueryHandler(video_10, pattern='^video_10$'))

print("🤖 BOT VETRINA AVVIATO!")
app.run_polling()
EOF
