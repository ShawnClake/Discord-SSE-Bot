from discord import Embed


class Image:
    def __init__(self, url, keywords=[], quote = ''):
        self.url = url
        self.keywords = keywords
        self.quote = quote

    def getImageEmbed(self):
        return Embed().set_image(url=self.url)

