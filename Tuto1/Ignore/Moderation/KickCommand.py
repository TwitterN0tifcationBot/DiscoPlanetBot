import discord
from discord.ext import commands

class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', description='Kick a user from the server', usage='@user [reason]', example='@user spamming')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        if not reason:
            reason = "No reason provided"
        
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="🪐 Successfully Kicked!",
            description=f"You have successfully kicked {member.mention} for {reason}.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='⛔ Error 909',
                description='You do not have the required permissions to use this command.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(KickCommand(bot))
    guild.kick({member}, reason={reason}),