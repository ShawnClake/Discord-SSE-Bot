from discord.ext.commands.context import Context
from discord import Client


class AssignRole:

    @staticmethod
    async def role(ctx: Context):
        # Get the user who sent the command
        user = ctx.message.author
        await ctx.bot.send_message(ctx.message.channel, user)
