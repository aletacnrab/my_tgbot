# Echo Telegram Bot  
#### This bot echoes back any text message it receives, providing a simple demonstration of handling messages using the __python-telegram-bot__ library.  
---
1. __Import__ necessary modules from the python-telegram-bot library.
2. __Replace__ `'your_bot_token'` with the actual token of your Telegram bot.
3. __Define__ a function echo that retrieves the text of the received message and sends back an echo.
4. In the main function, __create__ an Updater object with the bot's token and get the dispatcher to register handlers.
5. __Register__ the echo handler to handle text messages (excluding commands).
5. __Start__ the bot polling for updates.
6. __Run__ the bot until a signal to stop is received.
---
Remember to replace `'your_bot_token'` with the actual __token__ of your Telegram bot.
