import os
from telegram.ext import *

API_KEY = ''


class MovingAverageBot:
    def __init__(self, img):
        self.img = img
        updater = Updater(API_KEY, use_context=True)
        dp = updater.dispatcher

        # Commands
        dp.add_handler(CommandHandler('start', self.start_command))
        dp.add_handler(CommandHandler('help', self.help_command))
        dp.add_handler(CommandHandler('custom', self.custom_command))

        # Messages
        dp.add_handler(MessageHandler(Filters.text, self.send_stock_photo))

        # Run the bot
        updater.start_polling()
        updater.idle()

    def start_command(self, update, context):
        update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

    def help_command(self, update, context):
        update.message.reply_text('Try typing anything and I will do my best to respond!')

    def custom_command(self, update, context):
        update.message.reply_text('This is a custom command, you can add whatever text you want here.')

    def send_stock_photo(self, update, context):
        context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=self.img, caption='STOCK')

        print("response sent !!")


# Run the programme
if __name__ == '__main__':
    IMG = open('IEX.png', 'rb')
    bot = MovingAverageBot(IMG)
