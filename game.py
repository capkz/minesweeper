import pygame

class Game():
    def __init__(self, board, windowSize):
        self.board = board
        self.windowSize = windowSize

    def run(self):
        #Initiate
        pygame.init()
        window = pygame.display.set_mode(self.windowSize)
        isRunning = True

        #Game loop
        while isRunning == True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    isRunning = False #TODO Add a prompt asking if user wants to quit their game in progress
            pygame.display.flip()
        pygame.quit()

