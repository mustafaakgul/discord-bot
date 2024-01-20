### Guide
* Go to link -> https://discord.com/developers/applications
* Create a new application
* Go to Bot tab and create a new bot
* Create a server
* Add the bot to the server
  * Go to developer portal page again
  * Go to OAuth2 tab and select bot and Administrator in Bot Permission in scopes in URL Generator
  * Discord has generated your application’s authorization URL with the selected scope and permissions
  * Copy the URL and paste it in your browser and select the server you want to add the bot to
  * Click Authorize
  * You will be redirected to your server and you will see your bot in the sidebar
* Let's code
  * First of all, you need to install discord.py by running pip install discord.py
  * Creating a Discord Authentication by creating an instance of Client boy.py
  * Create a copy from .env.base and rename it to .env by running cp .env.base .env
  * Use .env file to store your token from Discord Developer Portal Bot tab
  * To test your bot, run python bot.py
  * Integration with Discord APIs
  * HERE https://realpython.com/how-to-make-a-discord-bot-python/


### If you got certificate error, then run the following command
* Go to Desktop on Mac and click Go in Finder
* Click on Applications
* Click on Python3.x folder
* Click on Install Certificates.command
* This runs the command automatically
* But be aware that your virtual environment must be dependent on the THIS Python3.x version