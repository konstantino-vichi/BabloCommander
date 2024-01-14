import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

updater = Updater(token=os.environ['TBOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher


# Start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to your Daily Expense Tracker!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Add Expense
def add_expense(update, context):
    # Logic to add an expense
    pass

add_expense_handler = CommandHandler('addexpense', add_expense)
dispatcher.add_handler(add_expense_handler)

updater.start_polling()
