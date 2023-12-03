from telegram.ext import Updater, MessageHandler, Filters

# Telegram bot token (replace with your own token)
TOKEN = 'your_bot_token'

def echo(update, context):
    # Get the message text
    message_text = update.message.text
    
    # Echo back the received message
    update.message.reply_text(f"You said: {message_text}")

def main():
    # Create an Updater object and pass it your bot's token
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the echo handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
