import discord
from discord.ext.commands import bot
from discord.ext import commands

class mainCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rules", help = " - Display the server rules.")
    async def rules(self, ctx):
        embed = discord.Embed(title = "Rules", description = "Please read and adhere to the following rules carefully. Failing to do so could result in a server mute, kick, or ban.")
        embed.add_field(name="1.", value="No spreading of any discriminatory, hateful, racist, or sexist content in VC or text chats.", inline=False)
        embed.add_field(name="2.", value="Keep posts relevant to their respective chats.", inline=False)
        embed.add_field(name="3.", value="No NSFW content (eg. adult content, dark or violent content, etc.) in VC or text chats.", inline=False)
        embed.add_field(name="4.", value="No spam (repetative messages in text chats, loud or repetative speaking in voice chats).", inline=False)
        embed.add_field(name="5.", value="If you observe an individual(s) breaking one of the aforementioned rules, report the situation to a server administrator.", inline=False)
        embed.set_footer(text = "MachoDroid")
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(mainCommands(bot))