import logging
from .utils import BotUtils

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Ativa o log das requisições.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class FreepikBot:
    def __init__(self, token):
        self.token = token
        self.application = ApplicationBuilder().token(self.token).build()
        self.start_handler = CommandHandler("freepik", self.start)
        self.application.add_handler(self.start_handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text
        bot_response = BotUtils.bot_response(user_message)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{bot_response}")

    def run(self):
        self.application.run_polling()