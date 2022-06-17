import pygame, os, sys
from board import Board
from button import Button

class Game:
    def __init__(self, difficulty):
        self.assets = None
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.windowSize = (800,900)
        pygame.display.set_caption('MineSweeper by Chagil Pekoz')
        self.screen = pygame.display.set_mode(self.windowSize)
        self.resetButton = None
        self.cellSize = (self.windowSize[0]+5) // self.board.getSize()[1], (self.windowSize[1]-95) // self.board.getSize()[0]
        self.loadAssets()

    def run(self):
        #Initiate
        pygame.init()
        isRunning = True
        #Game loop
        while isRunning == True:
            self.screen.fill((192, 192, 192))
            self.draw()
            self.topBarDraw()
            pygame.display.flip()
            if not self.board.getGameStatus()[0] == 0:
                pygame.time.wait(2000)
                if self.board.getGameStatus()[0] == -1: # If game is a loss
                    self.board.resetBoard() # Initiates reset back to initial state with the same bomb locations
                else: # Game is a win
                    self.board.resetBoard(newGame = True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] >= 100:
                    button = pygame.mouse.get_pressed(num_buttons=3) #Gets the button click
                    self.handleClickEvent(pygame.mouse.get_pos(), button)
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     if self.resetButton.clicked(event):
                #         self.board.resetBoard()
        pygame.quit()

    def topBarDraw(self):
        # Top bar is drawn here, the uncovered cells count, and the game status is shown here.
        font = pygame.font.Font('assets/Grand9K Pixel.ttf', 60)

        text = font.render(str(self.board.getNumUncoveredCells()), False, (255, 0, 0))
        self.screen.blit(text, (20,5))

        # self.resetButton = Button("Reset", (150,30), size=(100, 50))
        # self.resetButton.render(self.screen)

        text = font.render(str(self.board.getGameStatus()[1]).title(), False, (0, 0, 0))
        self.screen.blit(text, (200, 5))

    def draw(self):
        pos = (0, 100)
        for row in range (self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                cell = self.board.getCell((row,col))
                asset = self.assets[cell.getCell()]
                self.screen.blit(asset, pos)
                pos = pos[0] + self.cellSize[0], pos[1]
            pos = 0, pos[1] + self.cellSize[1]

    def loadAssets(self):
        # All the game assets (pngs) are loaded in here ready to be used during the game is running.
        self.assets = {}
        path = 'assets/'
        filenames = [f for f in os.listdir(path) if f.endswith('.png')]
        for name in filenames:
            imagename = os.path.splitext(name)[0]
            image = pygame.image.load(os.path.join(path, name))
            image = pygame.transform.scale(image, (int(self.cellSize[0]), int(self.cellSize[1])))
            self.assets[imagename] = image

    def handleClickEvent(self, pos, button):
        if self.board.getGameStatus()[0] != 0:
            return
        # We get which button was clicked, // for integer division
        index = (pos[1]-100) // self.cellSize[1], pos[0] // self.cellSize[0]
        if not index[0] < 0 and not index[1] < 0:
            cell = self.board.getCell(index)
            self.board.handleClickEvent(cell, button)
