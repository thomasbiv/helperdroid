import os
import requests
import discord
from mytoken import my_token
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.help import HelpCommand
from secret import client_id, client_secret, twitch_api_url, check_stream_url

isLive = False

GUILD_ID = 769713139729432586 #Insert your guild ID here
TWITCH_NOTIF_CHANNEL = 769713139729432590 

# Twitch API authorization
auth_response = requests.post(f'{twitch_api_url}oauth2/token', {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
})
auth_response.raise_for_status()
access_token = auth_response.json()['access_token']

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='^', intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=" your commands 🤖"))
    print("We have logged in as {0.user}".format(bot))
    bot.load_extension('mainCommands')
    check_twitch.start()
    

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
async def check_twitch():
    # Twitch API request
    streamer_username = 'machospacemangaming'
    headers = {'Authorization': f'Bearer {access_token}', 'Client-Id': client_id}
    params = {'user_login': streamer_username}
    response = requests.get(f'{check_stream_url}/streams', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()['data']
    channel = bot.get_channel(TWITCH_NOTIF_CHANNEL)
    global isLive

    # Check if streamer is live and post notification in Discord text channel
    if len(data) > 0:
        stream_info = data[0]
        stream_title = stream_info['title']
        stream_game = stream_info['game_name']
        print(f'{data[0]["user_name"]} is live!') # For debug purposes
        if channel is not None:
            if isLive == False:
                message = f'{streamer_username} is now live playing {stream_game}: {stream_title}! Check it out at https://www.twitch.tv/{streamer_username}'
                await channel.send(message)
                isLive = True
        else:
            print(f'Error. could not find channel with id {TWITCH_NOTIF_CHANNEL}')
    else:
        if isLive == True:
            isLive = False

        print(f'{streamer_username} is offline.') # For debug purposes


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

#check_twitch.start()
bot.run(my_token)