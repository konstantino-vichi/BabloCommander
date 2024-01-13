import os
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# Define states for the conversation
AMOUNT, CATEGORY, NOTES = range(3)
bot_token = os.getenv('KAPITAL_BOT_TOKEN')

def start_addexpense(update, context):
    update.message.reply_text("Please enter the expense amount:")
    return AMOUNT

def ask_for_category(update, context):
    # Store the amount in context.user_data
    context.user_data['amount'] = update.message.text
    update.message.reply_text("Please enter the expense category:")
    return CATEGORY

def ask_for_notes(update, context):
    # Store the category in context.user_data
    context.user_data['category'] = update.message.text
    update.message.reply_text("Any notes for the expense?")
    return NOTES

def save_expense(update, context):
    # Store the notes in context.user_data
    context.user_data['notes'] = update.message.text
    # Here you'll format and save the expense data to the JSON file
    update.message.reply_text("Expense saved.")
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

def main():
    updater = Updater(bot_token, use_context=True)

    # Define the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('addexpense', start_addexpense)],
        states={
            AMOUNT: [MessageHandler(Filters.text & ~Filters.command, ask_for_category)],
            CATEGORY: [MessageHandler(Filters.text & ~Filters.command, ask_for_notes)],
            NOTES: [MessageHandler(Filters.text & ~Filters.command, save_expense)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
