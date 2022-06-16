class Cell: # Possible States: 1) Not Clicked, Clicked, Flagged
    def __init__(self, isMine, coords):
        self.isMine = isMine
        self.isUncovered = False
        self.isFlagged = False
        self.coords = (coords[0], coords[1])
        self.neighbors = None
        self.neighborMinesCount = 0

    def getIsMine(self):
        return self.isMine

    def getIsUncovered(self):
        return self.isUncovered

    def getIsFlagged(self):
        return self.isFlagged

    def getCellCoords(self):
        return self.coords

    def toggleIsUncovered(self):
        self.isUncovered = True

    def toggleIsFlagged(self):
        self.isFlagged = not self.isFlagged

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setMineCount()

    def setMineCount(self):
        for cell in self.neighbors:
            if cell.getIsMine() is True:
                self.neighborMinesCount += 1

    def getCell(self):
        if self.isFlagged:
            return "flag_cell"
        elif self.isMine is False:
            if self.neighborMinesCount == 0:
                if self.isUncovered == False:
                    return "default_cell"
                return "0"
            else:
                return str(self.neighborMinesCount)

        elif self.isMine is True:
            if self.isUncovered is False:
                return "unclicked_mine"
            else:
                return "clicked_mine"
