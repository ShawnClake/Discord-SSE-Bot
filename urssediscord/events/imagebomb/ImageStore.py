from urssediscord.events.imagebomb.Image import Image


def substring_indexes(substring, string):
    """
    Generate indices of where substring begins in string

    >>> list(substring_indexes('me', "The cat says meow, meow"))
    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:
            break  # All occurrences have been found
        yield last_found


class ImageStore:
    def __init__(self):
        self.images = []

    def addImage(self, image: Image):
        self.images.append(image)

    def getImagesFromKeywords(self, input: str):
        selected = []
        for image in self.images: # Loop through each image type
            for keyword in image.keywords: # Loop through the keywords on each image
                search = list(substring_indexes(keyword, input)) # Retrieve all the indexes of found matches for the keywords
                for result in search:
                    if len(keyword) > len(input): # If they keyword is longer than the input then skip it
                        continue
                    if result == 0 and len(keyword) == len(input): # If the keyword is the entire message
                        selected.append(image)
                    elif result == 0 and len(keyword) < len(input) and input[len(keyword)] == ' ': # If the message begins with the keyword and has at least a space after it
                        selected.append(image)
                    elif result > 0 and input[result - 1] == ' ' and (result + len(keyword)) == len(input): # If the keyword are the final characters of a message and is preceeded by a space
                        selected.append(image)
                    elif result > 0 and input[result - 1] == ' ' and (result + len(keyword)) < len(input) and input[result + len(keyword)] == ' ': # If the keyword is in the middle of a message and has spaces on either side of it
                        selected.append(image)
        return selected
