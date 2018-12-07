class AsciiPrinter:
    def __init__(self):
        self.lines = []

    def addLine(self, line):
        self.lines.append(line)

    def clear(self):
        self.lines = []

    def print(self):
        print(self.getPrint())

    def getPrint(self):
        ascii = ''
        for line in self.lines:
            if len(ascii) > 0:
                ascii += '\n'
            ascii += line
        return ascii
