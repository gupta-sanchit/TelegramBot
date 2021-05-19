import os
from dotenv import load_dotenv
from telegram.ext import *

load_dotenv()


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


class MovingAverageBot:
    def __init__(self, img, symbol):
        self.img = img
        self.symbol = symbol
        updater = Updater(os.getenv('API_KEY'), use_context=True)
        dp = updater.dispatcher

        # Commands
        dp.add_handler(CommandHandler('start', start_command))
        dp.add_handler(CommandHandler('help', help_command))
        dp.add_handler(CommandHandler('custom', custom_command))

        # Messages
        dp.add_handler(MessageHandler(Filters.text, self.send_stock_photo))

        # Run the bot
        updater.start_polling()
        updater.idle()

    def send_stock_photo(self, update, context):
        text = str(update.message.text).lower()
        print(update.message.chat.id)

        # Bot response

        update.message.reply_text('response')
        context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=self.img, caption=self.symbol)

        print("response sent !!")


if __name__ == '__main__':
    IMG = open('IEX.png', 'rb')
    bot = MovingAverageBot(img=IMG, symbol='ABC')
