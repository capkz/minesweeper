from cell import Cell
import random, numpy as np

class Board:
    def __init__(self, difficulty, minePos = None):
        self.difficulty = difficulty
        self.mineCount = 0
        match difficulty:
            case "beginner":
                self.size = (9, 9)
                self.mineCount = 10
            case "intermediate":
                self.size = (16, 16)
                self.mineCount = 40
            case "hard":
                self.size = (22, 22)
                self.mineCount = 99
        self.cellCount = self.size[0] * self.size[1]
        self.board = []
        self.numUncoveredCells = 0
        self.status = 0 # -1 means lost, 0 means in progress, 1 means win

        # This is for reset functionality, if reset is used, we take the list from the previous game instance and
        # reinstate another match with that. If not, we get a fresh batch of random positions.
        self.randomMinePos = minePos
        if self.randomMinePos is None:
            self.randomMinePos = self.__randomMinePos()
        self.setBoard()

    def setBoard(self):
        print(self.randomMinePos)

        yCoord = 0
        for row in range(self.size[0]):
            row = []
            xCoord = 0
            for col in range(self.size[1]):
                if (xCoord, yCoord) in self.randomMinePos:
                    isMine = True
                else:
                    isMine = False
                cell = Cell(isMine, coords=(xCoord, yCoord))
                row.append(cell)
                xCoord += 1
            self.board.append(row)
            yCoord += 1
        self.setNeighbors()

    def __randomMinePos(self):
        # This method returns a list of coordinates for the mine to spawn
        # Generates 2 different lists for both x and y, zips them together and turns them into a list. Turning that
        # list into a set clears out duplicates, and we change that back to a list.
        # Later on it is checked if any duplicates were deleted from the list, if so, we replace those empty spots
        # with new numbers with new unique ones.
        xPos = np.random.choice(range(0, self.size[0]), self.mineCount).tolist()
        yPos = np.random.choice(range(0, self.size[1]), self.mineCount).tolist()
        randomMinePos = list(set(list(zip(xPos,yPos)))) # Turning the list into a set gets rid of any possible duplicates

        if len(randomMinePos) != self.mineCount: #If we have duplicates deleted we try to replace them until we have the right amount
            while len(randomMinePos) != self.mineCount:
                xPos = np.random.choice(range(0, self.size[0]), 1)
                yPos = np.random.choice(range(0, self.size[1]), 1)
                randomMinePos.append((int(xPos), int(yPos)))
                randomMinePos = list(set(randomMinePos))

        return randomMinePos

    def setNeighbors(self):
        # This method gets the neighbors list of each cells from the method getListNeighbors and stores that in the
        # each cell's object.
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row,col))
                neighbors = self.getListNeighbors((row, col))
                cell.setNeighbors(neighbors)

    def getListNeighbors(self, pos):
        # This method gets the list of each neighbors. It is made sure to not get out of bounds cells or itself.
        neighbors = []
        for row in range(pos[0] - 1, pos[0] + 2):
            for col in range(pos[1] - 1, pos[1] + 2):
                isOutOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1] # Check if the neighbor actually exists
                isItself = row == pos[0] and col == pos[1] # Don't count itself
                if isOutOfBounds == False and isItself == False:
                    neighbors.append(self.getCell((row, col)))
        return neighbors

    def getSize(self):
        # Returns the (x, y) size of the board.
        return self.size

    def getCell(self, pos):
        # Returns the cell object stored within the provided coords on the board.
        return self.board[pos[0]][pos[1]]


    def getGameStatus(self):
        # Returns the game's status and the status message.
        match self.status:
            case -1:
                return -1, "lost, resetting!"
            case 0:
                return 0, "in progress"
            case 1:
                return 1, "Congrats!"

    def getNumUncoveredCells(self):
        # Returns the uncovered cell count.
        return self.numUncoveredCells

    def resetBoard(self):
        # Resets the board to its initial state with the same bomb placements.
        # Loops through each cell and runs the reset method within them, lastly it
        # initializes the board's init method to reset it back to its initial state.
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row,col))
                cell.reset()
        self.__init__(self.difficulty,self.randomMinePos)

    def handleClickEvent(self, cell, button):
        # Most of the game logic runs when the handleClickEvent is triggered.

        # if left click is pressed, uncover unless it was flagged or it was previously uncovered
        if button[0] and not cell.getIsFlagged() and not cell.getIsUncovered():
            cell.toggleIsUncovered()
            # if the uncovered cell was a mine, game is lost
            if cell.getIsMine():
                self.status = -1
            elif cell.neighborMinesCount == 0:
                for neighbor in cell.getNeighbors():
                    if neighbor.getIsMine() == False and neighbor.getIsUncovered() == False:
                        self.handleClickEvent(neighbor, button = (1, 0, 0))
            self.numUncoveredCells += 1
            if self.numUncoveredCells + self.mineCount == self.cellCount:
                self.status = 1 # If the uncovered cells + mines equal to total, win condition
        # if right click is pressed, flag it unless it was previously uncovered
        elif button[2] and cell.getIsUncovered() == False:
            cell.toggleIsFlagged()
        else:
            pass
