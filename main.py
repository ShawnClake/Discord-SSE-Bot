import discord
from discord.ext import commands
import random
from urssediscord.commands.AssignRole import AssignRole
from urssediscord.commands.StackOverflow import StackOverflow
from urssediscord.events.ImageBomb import ImageBomb

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

@bot.event
async def on_message(message):

    msg = message.content.lower()

    yas_terms = ["yasser",
                 "capstone",
                 "4yp",
                 "fourth year project",
                 "networks",
                 "testing",
                 "test suite",
                 "advisor",
                 "project day"]

    trev_terms = ["trevor",
                  "lab"]

    karim_terms = ["karim",
                   "naqvi"]

    craig_terms = ["linux",
                   "craig",
                   "gelowitz"]

    if any(string in msg for string in yas_terms):
        await ImageBomb.yas_bomb(message, bot)

    if any(string in msg for string in trev_terms):
        await ImageBomb.trev_bomb(message, bot)

    if any(string in msg for string in karim_terms):
        await ImageBomb.karim_bomb(message, bot)

    if any(string in msg for string in craig_terms):
        await ImageBomb.craig_bomb(message, bot)


@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')


bot.run(config.app.token)
