import discord
from discord.ext import commands
import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

class Imagine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='imagine', description='Generate an image from a prompt', usage='imagine <prompt>')
    async def imagine(self, ctx, *, prompt: str):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            embed = discord.Embed(
                title="Imagine",
                description=f"Prompt: {prompt}",
                color=discord.Color.blue()
            )
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(Imagine(bot))