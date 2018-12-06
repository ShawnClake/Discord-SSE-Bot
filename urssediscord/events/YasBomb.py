from discord import Embed

class YasBomb:
    @staticmethod
    async def yas_bomb(message, bot):
        embed = Embed().set_image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/yasser-morgan.jpg")
        await bot.send_message(message.channel, embed=embed)
