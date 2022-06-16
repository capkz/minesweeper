from game import Game
from board import Board
import os
#Temporary settings initiation
difficulty = "beginner" #beginner, intermediate or hard
windowSize = (800,800) #Will be determined by the difficulty setting later, temporary

game = Game(difficulty, windowSize)
game.run()