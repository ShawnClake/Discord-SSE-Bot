from discord import Embed

class ImageBomb:
    @staticmethod
    async def yas_bomb(message, bot):
        embed = Embed().set_image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/yasser-morgan.jpg")
        await bot.send_message(message.channel, embed=embed)

    @staticmethod
    async def trev_bomb(message, bot):
        embed = Embed().set_image(
            url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/trevor-douglas.jpg")
        await bot.send_message(message.channel, embed=embed)

    @staticmethod
    async def karim_bomb(message, bot):
        embed = Embed().set_image(
            url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/karim-naqvi.jpg")
        await bot.send_message(message.channel, embed=embed)

    @staticmethod
    async def craig_bomb(message, bot):
        embed = Embed().set_image(
            url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/craig-gelowitz.jpg")
        await bot.send_message(message.channel, embed=embed)


