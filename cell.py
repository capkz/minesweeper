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

    def getNeighbors(self):
        return self.neighbors

    def toggleIsUncovered(self):
        self.isUncovered = True

    def toggleIsFlagged(self):
        self.isFlagged = not self.isFlagged

    def setNeighbors(self, neighbors):
        # Sets the neighbors for the cell and runs setMineCount to get how many mines are around that cell
        self.neighbors = neighbors
        self.setMineCount()

    def setMineCount(self):
        # Checks if the neighbor cells have mines, if they do, increases the amount of mine neighbors of the cell.
        for cell in self.neighbors:
            if cell.getIsMine() is True:
                self.neighborMinesCount += 1

    def getCell(self):
        # Gets the asset that has to be shown for the cell depending on its state.
        if self.isUncovered == False:
            if self.isFlagged:
                return "flag_cell"
            return "default_cell"
        elif self.isMine is False:
            if self.neighborMinesCount == 0:
                return "0"
            else:
                return str(self.neighborMinesCount)

        elif self.isMine is True:
            if self.isUncovered is False:
                return "unclicked_mine"
            else:
                return "clicked_mine"

    def reset(self):
        # Ran from board.py for resetting the game to its initial phase with the same bomb locations.
        self.__init__(self.isMine, self.coords)