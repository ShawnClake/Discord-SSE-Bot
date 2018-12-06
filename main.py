from discord.ext import commands
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

@bot.event
async def on_member_join(user):
    user.send("Welcome to our discord server! Give yourself roles by typing /role in any text channel.")

bot.run(config.app.token)
