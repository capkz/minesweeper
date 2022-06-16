import pygame, os
from board import Board
class Game:
    def __init__(self, difficulty, windowSize):
        self.assets = None
        self.board = Board(difficulty)
        self.windowSize = windowSize
        self.screen = pygame.display.set_mode(self.windowSize)
        self.cellSize = self.windowSize[0] // self.board.getSize()[1], self.windowSize[1] // self.board.getSize()[0]
        self.loadAssets()

    def run(self):
        #Initiate
        pygame.init()
        isRunning = True
        #Game loop
        while isRunning == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False #TODO Add a prompt asking if user wants to quit their game in progress
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.mouse.get_pressed(num_buttons=3) #Check for right click, which is a flag
                    self.handleClickEvent(pygame.mouse.get_pos(), button)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            if not self.board.getGameStatus() == "in progress":
                isRunning = False
        pygame.quit()

    def draw(self):
        pos = (0,0)
        for row in range (self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                cell = self.board.getCell((row,col))
                asset = self.assets[cell.getCell()]
                self.screen.blit(asset, pos)
                pos = pos[0] + self.cellSize[0], pos[1]
            pos = 0, pos[1] + self.cellSize[1]

    def loadAssets(self):
        self.assets = {}
        path = 'assets/'
        filenames = [f for f in os.listdir(path) if f.endswith('.png')]
        for name in filenames:
            imagename = os.path.splitext(name)[0]
            image = pygame.image.load(os.path.join(path, name))
            image = pygame.transform.scale(image, (int(self.cellSize[0]), int(self.cellSize[1])))
            self.assets[imagename] = image

    def handleClickEvent(self, pos, button):
        # We get which button was clicked, // for integer division
        index = pos[1] // self.cellSize[1], pos[0] // self.cellSize[0]
        cell = self.board.getCell(index)
        self.board.handleClickEvent(cell, button)