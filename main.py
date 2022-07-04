import discord
from mytoken import my_token
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='^')
bot.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=" your commands 🤖"))
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
    guild = client.get_guild(750800943720824954)
    channel = client.get_channel(992579689845637140)
    embed = discord.Embed(title = "***New Member***", description = f"Thanks {member.mention} for joining! Welcome to {guild.name}!")
    embed.set_footer(text = "MachoDroid")
    await channel.send(embed = embed)

    #Private message to user
    await member.send("Welcome to the Space Station!")
    await member.send("Insert some boilerplate rules here.")

# @bot.event
# async def on_member_join(member):
#     await member.send("Welcome to the Space Station!")
#     await member.send("Insert some boilerplate rules here.")

@bot.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = "***Help***", description = "I'll put stuff here soon I swear")
    embed.set_footer(text = "MachoDroid")
    await ctx.send(embed = embed)

client.run(my_token)