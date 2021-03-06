from discord.ext.commands import Bot


class StackOverflow:
    @staticmethod
    async def so(ctx):
        # Parse the sent in command and split the command in whitespace.
        query = ctx.message.content.replace('/so ', '').replace(' ', '+').replace('/', '+')

        if query:
            link = "https://stackoverflow.com/search?q=" + query
            await ctx.message.channel.send(link)
        else:
            # Get the last message in the channel
            bot: Bot = ctx.bot
            ignoreFirst = True
            async for message in ctx.message.channel.history(limit=25):
                if (not ignoreFirst) and message.content[:3] == "/so":
                    return
                if (not ignoreFirst) and message.author.name != "UR SSE Bot":
                    link = "https://stackoverflow.com/search?q=" + message.content.replace(' ', '+').replace('/', '+')
                    await ctx.message.channel.send(message.author.mention + " " + link)
                    return
                ignoreFirst = False
