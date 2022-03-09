import discord
from discord.ext import commands
class Based(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.command()
    async def test(self, message):
     
        
       embed = discord.Embed(
           title = 'Las reglas',
           description = 'Fallar el seguimiento de estas regulaciones puede llevaros a ser removidos del servidor de forma permanente',
           colour = 1810143
           )
       embed.add_field(name='Regla 1', value='Queda prohibida cualquier iteración de la palabra "Astolfo" o sus variaciones', inline=False)
       embed.add_field(name='Regla 2', value='Queda prohibida cualquier iteración de cualquier personaje comúnmente conocido como "Astolfo"', inline=False)
       embed.add_field(name='Regla 3', value='Mantener respeto a todo miembro de este servidor, las bromas serán aceptadas pero solo cuando el bromista y su víctima estén en acuerdo', inline=False)
       embed.add_field(name='Regla 4',value='Utilicen de manera propia los canales de texto y de voz, pueden encontrar información sobre su uso en el canal de #información',inline=False)
       embed.set_footer(text='والدتك كبيرة في السن لدرجة أنها طلبت القرآن مسبقا')
       embed.set_author(name='Preußen', icon_url=message.author.avatar_url)
       
       
       
       
       await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Based(client))