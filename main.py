from discord.ext import commands
from urssediscord.commands.AssignRole import AssignRole
from urssediscord.commands.StackOverflow import StackOverflow
from urssediscord.events.imagebomb.ImageBomb import ImageBomb
from urssediscord.commands.Fork import Fork
import discord

from pymlconf import Root

config = Root()
config.load_file('config/app.yaml')

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='/', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def role(ctx):
    await AssignRole.role(ctx)


@bot.command(pass_context=True)
async def so(ctx):
    await StackOverflow.so(ctx)


@bot.command(pass_context=True)
async def fork(ctx):
    await Fork.fork(ctx)


@bot.event
async def on_message(message):
    if message.author.name != "UR SSE Bot":
        await ImageBomb.bomb(message)
        await bot.process_commands(message)


@bot.event
async def on_member_join(user):
    pass

    # await bot.server.create_channel(server, user.name, type=discord.ChannelType.text)
    #
    # everyone_perms = discord.PermissionOverwrite(read_messages=False)
    # my_perms = discord.PermissionOverwrite(read_messages=True)
    #
    # everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    #
    # user.send("Welcome to our discord server! Give yourself roles by typing /role in any text channel.")


bot.run(config.app.token)
