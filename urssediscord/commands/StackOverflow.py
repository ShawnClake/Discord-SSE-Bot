from discord.ext.commands import Bot

class StackOverflow:
    @staticmethod
    async def so(ctx):
        # Parse the sent in command and split the command in whitespace.
        query = ctx.message.content.replace('/so', '').replace(' ', '+').replace('/', '+')

        if query:
            link = "https://stackoverflow.com/search?q=" + query
            await ctx.bot.say(link)
        else:
            # Get the last message in the channel
            bot: Bot = ctx.bot
            async for message in bot.logs_from(ctx.message.channel, limit=2):
                link = "https://stackoverflow.com/search?q=" + message.content.replace(' ', '+').replace('/', '+')
            await ctx.bot.say(link)
