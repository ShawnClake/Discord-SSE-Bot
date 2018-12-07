from discord.ext import commands
from urssediscord.commands.AssignRole import AssignRole
from urssediscord.commands.StackOverflow import StackOverflow
from urssediscord.events.imagebomb.ImageBomb import ImageBomb
from urssediscord.commands.Fork import Fork
from urssediscord.utilities.DiscordAsciiPrinter import DiscordAsciiPrinter

from pymlconf import Root

config = Root()
config.load_file('config/app.yaml')


class SSEBot(commands.Bot):
    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        super().__init__(command_prefix, formatter, description, pm_help, **options)
        self.add_cog(StandardCommands(self))

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.name != "UR SSE Bot":
            await ImageBomb.bomb(message)
            await self.process_commands(message)
            # await self.bot.process_commands(message)

    async def on_member_join(self, user):
        user.send("Welcome to our discord server! Give yourself roles by typing /role in any text channel.")


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

    @commands.command()
    async def test(self, ctx):
        dap = DiscordAsciiPrinter()
        dap.addLine("         ___ skill 2")
        dap.addLine("skill 1 /")
        dap.addLine("        \\")
        dap.addLine("         --- skill 3")
        await ctx.message.channel.send(content=dap.getPrint())


client = SSEBot(command_prefix='/', description='UR SSE Discord Bot')
client.run(config.app.token)
