import os, discord, random
from discord.ext import commands

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fire")
    async def shoot(self, ctx):
        # Check if user is in a voice channel
        if ctx.author.voice is None:
            await ctx.send("You have to be in a channel to use this command.")

        # Pick a random user in the voice channel
        voice_channel = ctx.author.voice.channel
        shot_user = random.choice(voice_channel.members)

        # Prioritize nickname over username
        if shot_user.nick is None:
            shot_user.nick = shot_user.name

        # Remove User from voice channel and annonce them dead in text chat
        await shot_user.move_to(None)
        await ctx.send("Bang! {} was shot dead.".format(shot_user.nick))
 
def setup(bot):
    bot.add_cog(general(bot))