import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def join(self,ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            await ctx.send('Bruh, you need to be in a voice channel')
        finally:
            await ctx.send('Joe momma')
    @commands.command()
    async def leave(self,ctx):
        try:
            await ctx.voice_client.disconnect()
        except:
            await ctx.send('Mah dude, I\'m not even in a voice channel but I did channel JOE MOMMA')
    @commands.command()
    async def play(self, ctx, url):
        if ctx.voice_client == None:
            try:
               await ctx.author.voice.channel.connect()
            except:
                await ctx.author.send('I played with joe momma')
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('I pause our session with Joe momma, this better be worth it...')
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.author.send('I resumed Joe momma')
    @commands.command()
    async def loop(self, ctx):
        await ctx.author.send('Deez nuts can loop around Joe momma') 
    

def setup(client):
    client.add_cog(Music(client))

