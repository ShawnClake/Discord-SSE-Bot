from urssediscord.utilities.DiscordAsciiPrinter import DiscordAsciiPrinter
from discord.ext import commands


class SkillTreeCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        dap = DiscordAsciiPrinter()
        dap.addLine("         ___ skill 2                                  skill 4")
        dap.addLine("skill 1 /")
        dap.addLine("        \\")
        dap.addLine("         --- skill 3")
        await ctx.message.channel.send(content=dap.getPrint())
