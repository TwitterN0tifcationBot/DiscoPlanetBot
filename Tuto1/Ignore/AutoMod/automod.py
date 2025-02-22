import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.keywords = ["Nig", "Niggar", "Fuck"]  # Add your keywords here

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        for keyword in self.keywords:
            if keyword in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention}, your message contained a prohibited word and was deleted.")
                return

def setup(bot):
    bot.add_cog(AutoMod(bot))