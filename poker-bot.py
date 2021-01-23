#import libraries
import discord
from discord.ext.commands import Bot

#Your bot token
TOKEN="ask"

#create bot object
client = Bot(command_prefix="!")

#define func that is run on the on_message event
@client.event
async def on_message(message):
    print(message.author.id)
    print(message.content)
    if message.author.id != 802584001801748532:
        await message.channel.send("i recieved a message!")

client.run(TOKEN)
