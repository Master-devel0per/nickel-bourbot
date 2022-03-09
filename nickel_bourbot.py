import discord
from discord.ext import commands
import music
import economy
import based
from env import token





client = commands.Bot(command_prefix='%', intents = discord.Intents.all())
cogs = [music, economy, based]
for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



   


client.run(token)

       
                

