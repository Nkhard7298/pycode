from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update,context):
    update.message.reply_text('Hello, Calci welcomes you. Please enter the expression which needs to be computed by writing /math followed by expression.')

def math(update,context):
    """Echo the user message."""
    try:
    	update.message.reply_text(eval(update.message.text[6:]))
    except:
    	update.message.reply_text('Invalid expression')


updater = Updater('1231149355:AAHMIb0g_UyZYzeu-TQx0E9plca15bM7fSo', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,math))

updater.start_polling()
updater.idle()