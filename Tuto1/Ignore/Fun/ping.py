import discord
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', description='Ping command', usage='ping', category='Fun')
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!",
            description=f"Latency: {round(self.bot.latency * 1000)}ms",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(PingCommand(bot))