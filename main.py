from discord.ext import commands
from urssediscord.commands.AssignRole import AssignRole
from urssediscord.commands.StackOverflow import StackOverflow
from urssediscord.events.imagebomb.ImageBomb import ImageBomb
from urssediscord.commands.Fork import Fork
from urssediscord.utilities.DiscordAsciiPrinter import DiscordAsciiPrinter
import discord

from pymlconf import Root

config = Root()
config.load_file('config/app.yaml')


class SSEBot(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        description = 'UR SSE Discord Bot'
        self.bot = commands.Bot(command_prefix='/', description=description)

    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.name != "UR SSE Bot":
            await ImageBomb.bomb(message, self.bot)
            await self.bot.process_commands(message)

    async def on_member_join(self, user):
        user.send("Welcome to our discord server! Give yourself roles by typing /role in any text channel.")

    @commands.command(pass_context=True)
    async def role(self, ctx):
        await AssignRole.role(ctx)

    @commands.command(pass_context=True)
    async def so(self, ctx):
        await StackOverflow.so(ctx)

    @commands.command(pass_context=True)
    async def fork(self, ctx):
        await Fork.fork(ctx)

    @commands.command(pass_context=True)
    async def test(self, ctx):
        dap = DiscordAsciiPrinter()
        dap.addLine("         ___ skill 2")
        dap.addLine("skill 1 /")
        dap.addLine("        \\")
        dap.addLine("         --- skill 3")
        await ctx.bot.send_message(destination=ctx.message.channel, content=dap.getPrint())


client = SSEBot()
client.run(config.app.token)
