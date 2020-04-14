# SpaceKingsDiscordBot
A simple card-drawing bot for the Space Kings RPG (https://supertry.itch.io/spacekings). Decks of cards are unique for each player.

### Things you probably need:
 - **Git** - You can pick it up [here](https://git-scm.com/download/) if you don't have it. You need it to clone the repo.
 - **Python** - You need this to run Python. The link is [here](https://www.python.org).
 - **PIP** - This is the python package manager. This comes along with the Python installation.

### Getting started:
Here are some quick, but detailed instructions on how to get the project running locally.
 - First, go to the [Discord Developers Page](https://discordapp.com/developers/docs/intro). This has a ton of good info you might need. Also it has a link to the [Applications Page](https://discordapp.com/developers/applications/me#top). Go there.
 - Make a new App by clicking on the circle with the plus inside.
 - Take your client ID from that page and use it in this URL: ```https://discordapp.com/oauth2/authorize?&client_id=<CLIENT ID>&scope=bot&permissions=0```
 - Get your _token_ from that page and save it for later.
 - Clone this repo to your local machine.
 - For Windows users, populate the token in the Start.bat script.
 - For non-Windows users, create a startup script with the token as the second argument.
 - Use Pip to install the discord module.
 - Run your startup script!

### Commands:
- /draw - This will draw the number of cards specified ("/draw 2"). In Space Kings, faces and aces are successes, Jokers are a failure, and the Queen Of Hearts is a critical success (1 + Charm successes)
  
