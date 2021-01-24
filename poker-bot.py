#import libraries
import discord
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()

#Your bot token
TOKEN=os.getenv("TOKEN")
BOT_ID =os.getenv("BOT_ID")
#create bot object
client = Bot(command_prefix="!")

players = []

#define func that is run on the on_message event
@client.event
async def on_message(message):
    if message.author.id != BOT_ID:
        if "!newgame" in message.content.lower():
            await message.channel.send("Welcome to a game of poker, type “sit” to join.")
        if "!sit" in message.content.lower():
            await add_player(message.author, message.channel)
        if "!startgame" in message.content.lower():
            await message.channel.send("New game started.")
        if "!players" in message.content.lower():
            await list_players(message.author)

async def list_players(user):
    playersInfo = "Players:\n"
    for player in players:
        playersInfo += mention(player) + "\n"
    await user.send(playersInfo)

def mention(user):
    return "<@" + str(user.id)  + ">"

async def add_player(user, channel):
    if(len(players) < 7):
        if(user in players):
            await user.send(mention(user) + ", you can only join the game once.")
        else:
            await channel.send(mention(user) + " joined game")
            players.append(user)
    else:
        await user.send("The game is full.")

client.run(TOKEN)
