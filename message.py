import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=f"Chat ID: {chat_id}")

def main():
    updater = Updater(token="6048941815:AAE6oiBrldHON1MQ61XQ1FbO66jH6DSXBEQ", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
