from cell import Cell
import random, numpy as np


class Board:
    def __init__(self, difficulty):
        match difficulty:
            case "beginner":
                self.size = (9, 9)
                mineCount = 10
            case "intermediate":
                self.size = (16, 16)
                mineCount = 40
            case "hard":
                self.size = (16, 30)
                mineCount = 99
        self.cellCount = self.size[0] * self.size[1]
        self.board = []
        self.setBoard(mineCount)

    def setBoard(self, mineCount):
        randomMinePos = self.__randomMinePos(mineCount)
        print(randomMinePos)
        xCoord = 0
        yCoord = 0
        for row in range(self.size[0]):
            row = []
            xCoord = 0
            for col in range(self.size[1]):
                if (xCoord, yCoord) in randomMinePos:
                    isMine = True
                else:
                    isMine = False
                cell = Cell(isMine, coords=(xCoord, yCoord))
                row.append(cell)
                xCoord += 1
            self.board.append(row)
            yCoord += 1
        self.setNeighbors()

    def __randomMinePos(self, mineCount): #This method returns a list of coordinates for the mine to spawn
        xPos = np.random.choice(range(0, self.size[0]), mineCount).tolist()
        yPos = np.random.choice(range(0, self.size[1]), mineCount).tolist()
        randomMinePos = list(set(list(zip(xPos,yPos)))) # Turning the list into a set gets rid of any possible duplicates

        if len(randomMinePos) != mineCount: #If we have duplicates deleted we try to replace them until we have the right amount
            while len(randomMinePos) != mineCount:
                xPos = np.random.choice(range(0, self.size[0]), 1)
                yPos = np.random.choice(range(0, self.size[1]), 1)
                randomMinePos.append((int(xPos), int(yPos)))
                randomMinePos = list(set(randomMinePos))

        return randomMinePos

    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row,col))
                neighbors = self.getListNeighbors((row, col))
                cell.setNeighbors(neighbors)

    def getListNeighbors(self, pos):
        neighbors = []
        for row in range(pos[0] - 1, pos[0] + 2):
            for col in range(pos[1] - 1, pos[1] + 2):
                isOutOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1] # Check if the neighbor actually exists
                isItself = row == pos[0] and col == pos[1] # Don't count itself
                if (isOutOfBounds == False and isItself == False):
                    neighbors.append(self.getCell((row,col)))
        return neighbors

    def getSize(self):
        return self.size

    def getCell(self, pos):
        return self.board[pos[0]][pos[1]]

    def handleClickEvent(self, cell, button):
        if button[0] and not cell.getIsFlagged() and not cell.getIsUncovered(): #if left click is pressed, uncover
            cell.toggleIsUncovered()
            print(cell.getCellCoords())
        elif button[2] and not cell.getIsUncovered(): #if right click is pressed, flag
            cell.toggleIsFlagged()