from urssediscord.utilities.AsciiPrinter import AsciiPrinter


class DiscordAsciiPrinter(AsciiPrinter):
    def getPrint(self):
        return '```' + super().getPrint() + '```'
