class Fork:
    @staticmethod
    async def fork(ctx):
        for i in range(0, 5):
            await ctx.bot.say(ctx.message.author.mention + " you're being fork bombed")
        await ctx.bot.say("The bot makers have planned for this and took the forks away")
