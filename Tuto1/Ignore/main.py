import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTM0MTY2MDU4Nzk0MzUyNjQyMA.Gx_ORm.x7wEwBNNaUr-8PliRLioKqs-CRX0D4RtJJNDKg'

# Intents are required for certain events
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)