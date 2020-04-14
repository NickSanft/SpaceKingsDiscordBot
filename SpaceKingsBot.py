import discord
import sys
import inspect
import random
import time
import CardUtils
from DeckOfCards import Deck
from discord.ext import commands
from discord.ext.commands import Bot

"""
This is the main script for the Guild Wars 2 Bot for a discord server.

In order to run this script, simply call this from the command line
with the first argument being your Bot Token from the Discord API.
"""

help_attrs = dict(hidden=True)
bot = Bot(command_prefix='/', help_attrs=help_attrs)
decksByUser = {}



"""
Bot Events
"""


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_read():
    print("bot logged in")

async def initDeck(user: str):
    decksByUser[user] = Deck()

"""
Bot Commands
"""
@bot.command()
async def draw(ctx, numCards: int):
    user = ctx.message.author.id

    if user not in decksByUser:
        await initDeck(user)

    numSuccesses = 0
    numFailures = 0

    await ctx.send("Drawing " + str(numCards) + "...")

    for i in range(0, numCards):
        card = decksByUser[user].drawCard()
        #if CardUtils.isSuccess(card.suit):
            #numSuccesses += 1
        #if CardUtils.isFailure(card.suit):
            #numFailures += 1
        await ctx.send("You drew: " + card.description + ". Cards left: " + str(len(decksByUser[user].cards)))
        time.sleep(1)
        if len(decksByUser[user].cards) == 0:
            await ctx.send("Out of cards! getting a new deck...")
            time.sleep(1)
            await initDeck(user)
    await ctx.send("Done drawing!") # Successes: " + str(numSuccesses) + ". Failures: " + str(numFailures)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

"""
Init script
"""
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        bot.run(sys.argv[1])
    else:
        print("A bot token was not provided, the script will now end!!!")