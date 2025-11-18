import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from utils.validators import is_valid_url
from seo.indexer import process_link

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.strip()

    if not is_valid_url(message):
        await update.message.reply_text("❌ Please send a valid URL.")
        return

    await update.message.reply_text(f"🔗 Link received:\n{message}\n\n⏳ Processing SEO indexing...")

    try:
        results = await process_link(message)
        response = "✅ Indexing complete:\n"
        for engine, status in results.items():
            icon = "✅" if status else "⚠️"
            response += f"{icon} {engine}\n"
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"❌ An error occurred during indexing:\n{e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
