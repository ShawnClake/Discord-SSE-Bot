from urssediscord.commands.handlers.AssignRole import AssignRole
from urssediscord.commands.handlers.StackOverflow import StackOverflow
from urssediscord.commands.handlers.Fork import Fork
from discord.ext import commands


class StandardCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role(self, ctx):
        await AssignRole.role(ctx)

    @commands.command()
    async def so(self, ctx):
        await StackOverflow.so(ctx)

    @commands.command()
    async def fork(self, ctx):
        await Fork.fork(ctx)
