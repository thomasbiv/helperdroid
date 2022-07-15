import discord
from mytoken import my_token
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

GUILD_ID = 750800943720824954 #Insert your guild ID here

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='^', intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=" your commands 🤖"))
    print("We have logged in as {0.user}".format(bot))
    bot.load_extension('mainCommands')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("^"):
        await message.add_reaction("👍")
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(GUILD_ID)
    channel = discord.utils.get(guild.channels, name='welcome')
    #channel = bot.get_channel(992579689845637140)
    embed = discord.Embed(title = "***New Member***", description = f"Thanks {member.mention} for joining! Welcome to {guild.name}!")
    embed.set_footer(text = "MachoDroid")
    await channel.send(embed = embed)

    #Private message to user
    await member.send("Welcome to the Space Station!")
    embed = discord.Embed(title = "Rules", description = "Please read and adhere to the following rules carefully. Failing to do so could result in a server mute, kick, or ban.")
    embed.add_field(name="1.", value="No spreading of any discriminatory, hateful, racist, or sexist content in VC or text chats.", inline=False)
    embed.add_field(name="2.", value="Keep posts relevant to their respective chats.", inline=False)
    embed.add_field(name="3.", value="No NSFW content (eg. adult content, dark or violent content, etc.) in VC or text chats.", inline=False)
    embed.add_field(name="4.", value="No spam (repetative messages in text chats, loud or repetative speaking in voice chats).", inline=False)
    embed.add_field(name="5.", value="If you observe an individual(s) breaking one of the aforementioned rules, report the situation to a server administrator.", inline=False)
    embed.set_footer(text = "MachoDroid")
    await member.send(embed=embed)

@bot.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = "***Help***", description = "For more information on a specific command, type ^help <command>")
    embed.add_field(name = "Commands", value="rules")
    embed.set_footer(text = "MachoDroid")
    await ctx.send(embed = embed)

@help.command()
async def rules(ctx):
    embed = discord.Embed(title = "***rules***", description = "Display the server rules.", color = 0xa09c9c)
    embed.add_field(name = "Syntax", value = "^rules")
    embed.set_footer(text = "MachoDroid")
    await ctx.send(embed = embed)

bot.run(my_token)