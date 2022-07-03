import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

bot = commands.Bot(command_prefix='^')
bot.remove_command("help")

@bot.event