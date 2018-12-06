from discord import Embed
import random


class Image:
    def __init__(self, url, keywords=[], quote = ''):
        self.url = url
        self.keywords = keywords
        self.quote = quote

    def getImageEmbed(self):
        if isinstance(self.url, list):
            url = random.choice(self.url)
        else:
            url = self.url
        return Embed().set_image(url=url)

