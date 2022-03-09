import discord
from discord.ext import commands
import pymongo
from env import db_uri
def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = db_uri
    client = MongoClient(CONNECTION_STRING)
    return client['node-stuff']
data_base = get_database()


class Econ(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
       
        with open('test.txt', 'a') as file:
            file.write('Joe momma')
            file.close()
    @commands.command()
    async def beg(self, message):
        await message.channel.send('Joe momma')
        
def setup(client):
    client.add_cog(Econ(client))