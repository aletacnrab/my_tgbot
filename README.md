# my_tgbot  
#### This bot echoes back any text message it receives, providing a simple demonstration of handling messages using the __python-telegram-bot__ library.  
---
1. Import necessary modules from the python-telegram-bot library.
2. Replace `'your_bot_token'` with the actual token of your Telegram bot.
3. Define a function echo that retrieves the text of the received message and sends back an echo.
4. In the main function, create an Updater object with the bot's token and get the dispatcher to register handlers.
5. Register the echo handler to handle text messages (excluding commands).
5. Start the bot polling for updates.
6. Run the bot until a signal to stop is received.
---
Remember to replace `'your_bot_token'` with the actual __token__ of your Telegram bot.
