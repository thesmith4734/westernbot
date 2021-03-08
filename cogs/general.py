import os, discord, random, asyncio
from discord.ext import commands

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fire")
    async def shoot(self, ctx):
        # Check if user is in a voice channel
        if ctx.author.voice is None:
            await ctx.send("You have to be in a channel to use this command.")
        else:
            # Pick a random user in the voice channel
            voice_channel = ctx.author.voice.channel
            shot_user = random.choice(voice_channel.members)

            # Prioritize nickname over username
            if shot_user.nick is None:
                shot_user.nick = shot_user.name

            # Remove User from voice channel and annonce them dead in text chat
            await shot_user.move_to(None)
            await ctx.send("Bang! {} was shot dead.".format(shot_user.nick))
    
    @commands.command(name="kill_aiden")
    async def kill_aiden(self, ctx):
        voice_channel = ctx.author.voice.channel
        for channel_member in voice_channel.members:
            if channel_member.name == "fludd":
                await channel_member.move_to(None)
                await ctx.send

    @commands.command(name="duel")
    async def duel(self, ctx, challenged_user: discord.Member):
        # Get challenger
        challenger_user = ctx.author

        # Check if user is in voice channel
        if ctx.author.voice is None:
            await ctx.send("You have to be in a channel to use this command.")
        elif len(ctx.author.voice.channel.members) < 2:
            await ctx.send("There needs to be more than one person in the channel")
        else:
            # Build target message
            target_list = ['1','2','3','4','5','6','7','8','9']
            target_string = " "
            target_num = random.choice(target_list)
            target_list.remove(target_num)

            # Countdown to post
            countdown = 3
            countdown_message = await ctx.send("Ready?")
            await asyncio.sleep(1)
            while countdown:
                await countdown_message.edit(content=countdown)
                countdown -= 1
                await asyncio.sleep(1)

            # Post the target message
            await countdown_message.edit(content="Draw")
            await ctx.send(target_string.join(target_list))

            # Create check based on target number
            def check(m):
                return m.content == target_num
            
            # Annonce winner and boot loser from channel
            msg = await ctx.bot.wait_for('message', check=check)
            await ctx.send('{.author.name} wins!'.format(msg))
            if msg.author == challenger_user:
                await ctx.send('Bang! {.name} wins! {.name} has been shot!'.format(challenger_user, challenged_user))
                await challenged_user.move_to(None)
            else:
                await ctx.send('Bang! {.name} wins! {.name} has been shot!'.format(challenged_user, challenger_user))
                await challenger_user.move_to(None)
 
def setup(bot):
    bot.add_cog(general(bot))