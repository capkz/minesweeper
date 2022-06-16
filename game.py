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
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        pos = (0,0)
        for row in range (self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                asset = self.assets['empty_cell']
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
        print('debug')