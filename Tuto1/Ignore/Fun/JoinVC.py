import discord
from discord.ext import commands

class JoinVC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joinvc', description='Join a voice channel', usage='', example='', aliases=['joinvc'])
    async def joinvc(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel.")

def setup(bot):
    bot.add_cog(JoinVC(bot))