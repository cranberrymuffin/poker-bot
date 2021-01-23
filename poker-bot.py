#import libraries
import discord
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()

#Your bot token
TOKEN=os.getenv("TOKEN")

#create bot object
client = Bot(command_prefix="!")

#define func that is run on the on_message event
@client.event
async def on_message(message):
    print(message.author.id)
    print(message.content)
    if message.author.id != 802584001801748532:
        if "!start" in message.content.lower():
            await message.channel.send("start game invoked!")

client.run(TOKEN)
