import discord
from mytoken import my_token
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.help import HelpCommand
from twitch import check_if_live

isLive = False

GUILD_ID = 769713139729432586 #Insert your guild ID here

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='^', intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=" your commands 🤖"))
    print("We have logged in as {0.user}".format(bot))
    bot.load_extension('mainCommands')
    twitch_live_notifs.start()

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


@tasks.loop(seconds=30)
async def twitch_live_notifs():
    global isLive
    channel = "MachoSpacemanGaming"
    stream = check_if_live(channel)
    text_chat = bot.get_channel(769713139729432590)
    if stream == "OFFLINE" and isLive == False:
        await text_chat.send(channel + " is offline.")
    elif stream != "OFFLINE" and isLive == True:
        await text_chat.send(channel + " is still live!")
    elif stream != "OFFLINE" and isLive == False:
        isLive = True
        await text_chat.send(channel + " is live!")
    elif stream == "OFFLINE" and isLive == 1:
        await text_chat.send(channel + " just went offline.")
        isLive = 0


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