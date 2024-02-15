import discord
import sys
import inspect
import random
import time
from DeckOfCards import Deck
from discord.ext import commands
from discord.ext.commands import Bot, CommandInvokeError

"""
This is the main script for the Space Kings Bot for a discord server.
"""

intents = discord.Intents.default()
intents.message_content = True
help_attrs = dict(hidden=True)
bot = Bot(command_prefix='/', help_attrs=help_attrs, intents=intents)
decksByUser = {}

notNumbersMessages = ["You really think numbers are letters, huh?",
                      "You should really come with a warning label.",
                      "You’re not stupid! You just have bad luck when you’re thinking."]
failureMessages = ["It couldn't be too bad, could it?",
                   "Maybe you'll just slip on a banana peel."]
criticalfailureMessages = ["Pray to your gods.",
                           "Aw man, am I gonna die?", "This is funny in a cosmic sort of way."]

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
    author = ctx.message.author
    user = author.id

    if user not in decksByUser:
        await initDeck(user)

    numSuccesses = 0
    numFailures = 0
    queenOfHearts = False

    await ctx.send("Drawing " + str(numCards) + " for " + author.name + "...")
    time.sleep(1)

    for i in range(0, numCards):
        card = decksByUser[user].drawCard()
        if card.isSuccess():
            numSuccesses += 1
        if card.isFailure():
            numFailures += 1
        if card.isQueenOfHearts():
            queenOfHearts = True

        await ctx.send(
            author.name + " drew: " + card.description + ". Cards left: " + str(len(decksByUser[user].cards)))
        time.sleep(1)

        if len(decksByUser[user].cards) == 0:
            await ctx.send("Out of cards! getting a new deck...")
            time.sleep(1)
            await initDeck(user)

    resultMessage = "```Total number of Successes: " + str(numSuccesses) + "\n"

    if (queenOfHearts):
        resultMessage += "Queen Of Hearts! Add your charm to the number of successes! \n"

    if (numFailures == 1):
        resultMessage += "1 failure. " + random.choice(failureMessages) + "\n"
    elif numFailures == 2:
        resultMessage += "2 failures. " + random.choice(criticalfailureMessages) + "\n"
    else:
        resultMessage += "No failures, phew. \n"

    resultMessage += "```"

    await ctx.send(resultMessage)


@bot.command()
async def roll(ctx, roll: str):
    try:
        rollnum = int(roll)
        if (rollnum < 1):
            userName = ctx.message.author.mention
            resultString = "{}, get outta here with that nonsense".format(userName)
        else:
            resultString = "You rolled a: " + str(random.randrange(1, rollnum))
    except ValueError:
        resultString = random.choice(notNumbersMessages)
    await ctx.send(resultString)


"""
Init script
"""
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        bot.run(sys.argv[1])
    else:
        print("A bot token was not provided, the script will now end!!!")
