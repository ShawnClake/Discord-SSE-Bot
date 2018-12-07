from discord.ext import commands
from urssediscord.commands.StandardCommands import StandardCommands
from urssediscord.commands.SkillTreeCommands import SkillTreeCommands
from urssediscord.events.imagebomb.ImageBomb import ImageBomb
from urssediscord.utilities.Roles import has_role
from urssediscord.events.OnReady import on_ready
from urssediscord.events.OnJoin import on_join

from pymlconf import Root

config = Root()
config.load_file('config/app.yaml')


class SSEBot(commands.Bot):
    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        super().__init__(command_prefix, formatter, description, pm_help, **options)
        self.add_cog(StandardCommands(self))
        self.add_cog(SkillTreeCommands(self))

    async def on_ready(self):
        # This command is commented out for now.
        # When starting the bot, this will give any user without a text channel their own text channel.
        #
        await on_ready(self)


        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.name != "UR SSE Bot" and has_role(message.author, 'SSE Insider'):
            await ImageBomb.bomb(message)
        if message.author.name != "UR SSE Bot" or message.content == '/help':
            await self.process_commands(message)

    async def on_member_join(self, user):
        await on_join(user)


client = SSEBot(command_prefix='/', description='UR SSE Discord Bot')
client.run(config.app.token)
