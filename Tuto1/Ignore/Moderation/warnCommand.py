import discord
from discord.ext import commands

class WarnCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', description='Warn a user', usage='warn <user> <reason>', category='Moderation')
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str = None):
        if not reason:
            await ctx.send("Please provide a reason for the warning.")
            return

        embed = discord.Embed(
            title="🪐 Successfully Warned!",
            description=f"You have successfully warned {member.mention} for {reason}.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='⛔ Error 909',
                description='You do not have the required permissions to use this command.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(WarnCommand(bot))