import pygame
from game import Game
from button import Button

BUTTON = (185,185,185)
HOVER = (145,145,145)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class MainMenu:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        self.windowSize = (800, 900)
        self.screen = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption('MineSweeper by Chagil Pekoz')
        self.screen = pygame.display.set_mode(self.windowSize)

    def run(self):
        pygame.init()
        font = pygame.font.Font('assets/Grand9K Pixel.ttf', 60)
        isRunning = True

        while isRunning == True:
            self.screen.fill((192, 192, 192))
            draw_text('Main Menu', font, (255, 255, 255), self.screen, 250, 120)

            beginnerButton = Button("Beginner", (300,300), size=(200, 50))
            intermediateButton = Button("Intermediate", (250,400), size=(300, 50))
            hardButton = Button("Hard", (300,500), size=(200, 50))


            if beginnerButton.clicked():
                beginnerButton.setFill(HOVER)
            if intermediateButton.clicked():
                intermediateButton.setFill(HOVER)
            if hardButton.clicked():
                hardButton.setFill(HOVER)

            beginnerButton.render(self.screen)
            intermediateButton.render(self.screen)
            hardButton.render(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if beginnerButton.clicked():
                        game = Game('beginner')
                        game.run()
                    if intermediateButton.clicked():
                        game = Game('intermediate')
                        game.run()
                    if hardButton.clicked():
                        game = Game('hard')
                        game.run()
            pygame.display.flip()
            self.mainClock.tick(60)
        pygame.quit()