import discord
import command

command.name = "gcreate"
command.aliases = ["giveawaycreate"]
command.description = "Create a giveaway."
command.usage = "gcreate <time> <prize>"
command.example = "gcreate 1d 1000 coins"
command.cooldown = 5
command.category = "Giveaways"
command.guildOnly = True
command.permissions = ["MANAGE_GUILD"]

@command.event

async def command(message, time, prize):
    embed = discord.Embed(title="🎉 Giveaway 🎉", description=f"React with 🎉 to enter!\nTime: {time}\nPrize: {prize}", color=discord.Color.random())
    embed.set_footer(text="Ends at")
    embed.timestamp = time
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction("🎉")
    await message.delete()
    await message.channel.send(f"🎉 Giveaway created in {msg.channel.mention}! 🎉")