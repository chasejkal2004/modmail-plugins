from datetime import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class MeLogger(commands.Cog):
    """Logs"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)

      @commands.Cog.listener()
      async def on_message(message):
   
        id = message.author.id
        msg = message.content
        msgid = message.id
        srvr = message.guild
        chnl = message.channel.id
        with open("slurs.txt") as file: 
         slurs = [slurs.strip().lower() for slurs in file.readlines()]
      
        if any(slurs in message.content.lower() for slurs in slurs):
         chl = client.get_channel(827434179708977172)
         if message.author.bot: return
         if message.channel.id == 706967371880857650: return
         await message.delete()
       
         embedVar= discord.Embed(title="Slur", description="<@" + str(id) + "> said a slur", color=0xFF0000)
         embedVar.add_field(name="Message", value=str(msg), inline=False)
         embedVar.add_field(name="Channel", value='<#' + str(chnl) + '>',inline=False)
         embedVar.add_field(name="Time", value=message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
         embedVar.add_field(name="User ID", value=str(id), inline=True)  
         await chl.send(embed=embedVar)
         reason = "Autokick"
         embed= discord.Embed(title="AutoKick")
         embed.add_field(name="What server?", value=message.guild, inline= False)
         embed.add_field(name="Reason", value=str(msg), inline= False)
         embed.add_field(name="Invite Back", value="You have been warned by staff if it happens again you will be permanently  banned [Invite Back](https://discord.gg/6amPbc2dEf)")
         await message.author.send(embed=embed)
         await message.author.kick(reason=reason)
def setup(bot):
    bot.add_cog(MeLogger(bot))
