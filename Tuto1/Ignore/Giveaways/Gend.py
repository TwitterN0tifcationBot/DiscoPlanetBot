import discord
import command

class Gend(command.Command):
command.name = "giveaway end"
command.aliases = ["gend"]
command.description = "Ends a giveaway."
command.usage = "gend <message ID>"
command.category = "Giveaways"
command.permissions = ["manage_guild"]

async def run(self, client, message, args):
    if not args:
        return await message.channel.send("Please provide a message ID.")
    try:
        giveaway = await client.giveaways.get(message.guild.id, args[0])
    except:
        return await message.channel.send("Invalid message ID.")
    if not giveaway:
        return await message.channel.send("Giveaway not found.")
    await giveaway.end()
    await message.channel.send("Giveaway ended.")