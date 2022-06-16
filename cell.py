class Cell: # Possible States: 1) Not Clicked, Clicked, Flagged
    def __init__(self, isBomb):
        self.isBomb = isBomb
        self.isClicked = False
        self.isFlagged = False

    def getIsBomb(self):
        return self.isBomb

    def getIsClicked(self):
        return self.isClicked

    def getIsFlagged(self):
        return self.isFlagged