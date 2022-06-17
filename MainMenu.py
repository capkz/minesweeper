import pygame
from game import Game
from button import Button

BUTTON = (185,185,185)
HOVER = (145,145,145)
QUIT = (255,0,0)
BEGINNER = (0,255,0)
INTERMEDIATE = (255,100,0)
HARD = (255,0,100)

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
        title_font = pygame.font.Font('assets/Grand9K Pixel.ttf', 100)
        footer = pygame.font.Font('assets/Grand9K Pixel.ttf', 20)
        isRunning = True

        while isRunning == True:
            self.screen.fill((192, 192, 192))
            draw_text('Main Menu', title_font, (255, 255, 255), self.screen, 150, 120)
            draw_text('Made by capkz, 2022', footer, (255, 255, 255), self.screen, 20, 850)

            beginnerButton = Button("Beginner", (300,300), size=(200, 50))
            intermediateButton = Button("Intermediate", (250,400), size=(300, 50))
            hardButton = Button("Hard", (300,500), size=(200, 50))
            quitButton = Button("Quit", (300, 600), size=(200, 50))

            if beginnerButton.clicked():
                beginnerButton.setFill(BEGINNER)
            elif intermediateButton.clicked():
                intermediateButton.setFill(INTERMEDIATE)
            elif hardButton.clicked():
                hardButton.setFill(HARD)
            elif quitButton.clicked():
                quitButton.setFill(QUIT)

            beginnerButton.render(self.screen)
            intermediateButton.render(self.screen)
            hardButton.render(self.screen)
            quitButton.render(self.screen)
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