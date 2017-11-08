from discord.ext import commands
import discord
import asyncio
import random

prefix = ['!', '.']
bot = commands.Bot(command_prefix='m.', description='Bot create by ManGoYT with Python')


extensions = [
    'cogs.subs',
    'cogs.subscommand',
    'cogs.helpcommand',
    'cogs.Channel',
    'cogs.AllCommands',
    'cogs.subscommandray',
    'cogs.subscommandabdel',
    'cogs.subscommandkifkif',
    'cogs.subscommandreaper',
    'cogs.react',
    'cogs.subscommandmango',
    'cogs.massdm',
]

@bot.event
async def on_ready():
    print('ByManGoYT')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')
    await bot.change_presence(game=discord.Game(name="m.help ✌"))	

bot.remove_command('help')


if __name__ == '__main__':
    for module in extensions:
        bot.load_extension(module)
    bot.run("MzMwMzcwNzIxODk5NDc5MDQy.DJb6Tg.XV8uuMtlOmVdkokwW_fEIdsZXpQ")