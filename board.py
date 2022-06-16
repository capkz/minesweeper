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
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                if [row, col] in randomMinePos:
                    isMine = True
                else:
                    isMine = False
                cell = Cell(isMine)
                row.append(cell)
            self.board.append(row)

    def __randomMinePos(self, mineCount): #This method returns a list of coordinates for the mine to spawn
        xPos = np.random.choice(range(0, self.size[0]), mineCount)
        yPos = np.random.choice(range(0, self.size[1]), mineCount)
        randomMinePos = list(set(list(zip(xPos,yPos)))) # Turning the list into a set gets rid of any possible duplicates

        if len(randomMinePos) != mineCount: #If we have duplicates deleted we try to replace them until we have the right amount
            while len(randomMinePos) != mineCount:
                xPos = np.random.choice(range(0, self.size[0]), 1)
                yPos = np.random.choice(range(0, self.size[1]), 1)
                randomMinePos.append((int(xPos), int(yPos)))
                randomMinePos = list(set(randomMinePos))

        return randomMinePos

    def getSize(self):
        return self.size
