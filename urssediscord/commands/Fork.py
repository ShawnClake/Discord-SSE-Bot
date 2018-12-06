class Fork:
    @staticmethod
    async def fork(ctx):
        name = ctx.message.content.replace('/fork', '').replace(' ', '')
        for i in range(0, 5):
            if len(name) < 1:
                name = ctx.message.author.mention
            await ctx.bot.say(name + " you're being fork bombed")
        await ctx.bot.say("The bot makers have planned for this and took the forks away")
