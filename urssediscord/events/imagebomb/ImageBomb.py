from urssediscord.events.imagebomb.ImageStore import ImageStore
from urssediscord.events.imagebomb.Image import Image

image_store = ImageStore()

image_store.addImage(
    image=Image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/yasser-morgan.jpg",
                keywords=["yasser",
                          "capstone",
                          "4yp",
                          "fourth year project",
                          "networks",
                          "testing",
                          "test suite",
                          "advisor",
                          "project day",
                          "yas money",
                          "automated testing"]))

image_store.addImage(
    image=Image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/trevor-douglas.jpg",
                keywords=["trevor",
                          "lab",
                          "no drinks or food"]))

image_store.addImage(
    image=Image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/karim-naqvi.jpg",
                keywords=["karim",
                          "naqvi"]))

image_store.addImage(
    image=Image(url="https://www.uregina.ca/engineering/faculty-staff/faculty/images/craig-gelowitz.jpg",
                keywords=["linux",
                          "microshaft",
                          "microsoft",
                          "craig",
                          "gelowitz"]))

image_store.addImage(image=Image(url="https://i.gyazo.com/7fb42b920cc36728d939737b9333ed05.png", keywords=["wilson", "hiroshima", "league of legends", "noob"], quote="Wilson: \"Come on guyss\""))


class ImageBomb:
    @staticmethod
    async def bomb(message, bot):
        images = image_store.getImagesFromKeywords(message.content.lower())
        for image in images:
            embed = image.getImageEmbed()
            await bot.send_message(message.channel, embed=embed, content=image.quote)  # Potentially need to await here, but doubtful
