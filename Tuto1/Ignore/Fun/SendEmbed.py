import discord
import command

command.name = "Send Embed"
command.description = "Send an embed message"
command.category = "Fun"
command.permissions = ["send_messages"]
command.usage = "sendembed <title> <description> <color>"
 embed.discord.embed(
    title={title},
    description={description},
    color={color},
)
await embed.send()