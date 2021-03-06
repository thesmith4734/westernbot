import os, discord, settings
from discord.ext.commands import Bot
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents, description='Permission Regulation Bot')

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)
    
    if message.content.startswith('$hello'):
        await message.channel.send('World!')

bot.load_extension("cogs.general")
bot.run(os.getenv('TOKEN'))
