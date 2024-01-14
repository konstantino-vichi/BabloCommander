from asyncio.log import logger
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

updater = Updater(token=os.environ["TBOT_TOKEN"], use_context=True)
dispatcher = updater.dispatcher


# Start Command
def start(update, context):
	welcome_message = (
		"Welcome to your Daily Expense Tracker!\n"
		"Use /addexpense to add a new expense.\n"
		"For example: /addexpense 80 baht for coffee"
	)
	context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


# Add Expense Command
def add_expense(update, context):
	# Placeholder for adding expense logic
	response_message = "Received your expense. We are processing it."
	context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)
	# Add logic to parse and store the expense here


add_expense_handler = CommandHandler("addexpense", add_expense)
dispatcher.add_handler(add_expense_handler)


# Format Command
def format(update, context):
	msg = "hey beatch"
	


# Error Handling
def error(update, context):
	# Log Errors caused by Updates
	logger.warning('Update "%s" caused error "%s"', update, context.error)


dispatcher.add_error_handler(error)

# Start Polling
updater.start_polling()
