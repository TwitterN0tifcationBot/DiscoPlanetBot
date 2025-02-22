import discord
import command 
from discord.ext import commands

command.name = 'ban'
command.description = 'Ban a user'
command.usage = 'ban <user> <reason>'

class BanCommand(commands.Cog):

    # Check if the user has the required permissions to use the command
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        if not reason:
            await ctx.send("Please provide a reason for the ban.")
            return

        embed = discord.Embed(
            title="🪐 Successfully Banned!",
            description=f"You have successfully banned {member.mention} for {reason}.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
        guild.ban({user}, reason={reason}),
+       await ctx.send(f"{member} has been banned for {reason}.")
+       await member.send(f"You have been banned from {guild} for {reason}.")

    # Handle the error if the user does not have the required permissions
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='⛔ Error 909',
                description='You do not have the required permissions to use this command.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)