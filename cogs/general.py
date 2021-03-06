import os, discord
from discord.ext import commands

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fire")
    async def shoot(self, ctx):
        await ctx.send("Pew")
 
 #       await ctx.send("List of members: {}".format(ctx.voice_client.members))

def setup(bot):
    bot.add_cog(general(bot))