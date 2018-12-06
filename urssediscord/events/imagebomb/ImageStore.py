from urssediscord.events.imagebomb.Image import Image


class ImageStore:
    def __init__(self):
        self.images = []

    def addImage(self, image: Image):
        self.images.append(image)

    def getImagesFromKeywords(self, input: str):
        selected = []
        for image in self.images:
            if any(string in input for string in image.keywords):
                selected.append(image)
        return selected
