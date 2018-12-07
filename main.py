from discord.ext import commands
from urssediscord.commands.StandardCommands import StandardCommands
from urssediscord.commands.SkillTreeCommands import SkillTreeCommands
from urssediscord.events.imagebomb.ImageBomb import ImageBomb


from pymlconf import Root

config = Root()
config.load_file('config/app.yaml')


class SSEBot(commands.Bot):
    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        super().__init__(command_prefix, formatter, description, pm_help, **options)
        self.add_cog(StandardCommands(self))
        self.add_cog(SkillTreeCommands(self))

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


client = SSEBot(command_prefix='/', description='UR SSE Discord Bot')
client.run(config.app.token)
