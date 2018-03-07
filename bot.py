class Bot(object):
    def __init__(self, id ):
        self.id = id
        self.score = 0
        self.DNA = None
        self.state = True

    def __lt__(self, other):
        if self.score < other.score:
            return 1
        return 0

    def __eq__(self, other):
        if self.score == other.score:
            return 1
        return 0

    def __gt__(self, other):
        if self.score > other.score:
            return 1
        return 0

    def taketest(self, testpaper):
        self.score = testpaper.test(self.DNA)

    def injectDNA(self, dn):
        self.DNA = dn

    def extractDNA(self):
        return self.DNA

    def getscore(self):
        return self.score

    def show(self):
        pass
