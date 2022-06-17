# MineSweeper
 PyGame implementation of MineSweeper
 
## 1. Introduction
This was a fun and challenging project that required me to learn PyGame to execute. I have learned along the way that I can use PyGame as functional or OOP, even though I prefer functional, I wanted to challenge myself and also refresh my OOP knowledge so I chose the OOP way. I realized that I was glad to choose the OOP way of coding MineSweeper because it was more maintainable.

For the technicality of the game, in short:
1. The player is greeted with "_MainMenu_" class, which initializes the "_Game_" class depending on the difficulty the player chooses.
2.  "_Game_" is the class that initializes the game, manages the front-end and the game loop, checking for changes every tick. It also loads the game assets and decides which cell the user has clicked on.
3.  "_Game_" class then initializes the "_Board_" class, which maintains the board, the cell placements, game logic and game status.
4.  "_Board_" class initializes multiple "_Cell_" classes, and places them on the board. Each "_Cell_" class stores information about themselves and their neighbors. They also hold the informationn needed about which asset to show depending on their state.

All of the important methods and algorithms should be explained and clarified with comments within them in the files. 

## 2. Instructions
This section shows how to launch the game.

1. Clone the repository
2. Make sure Python is installed.

3. Launch CMD/Terminal in the minesweeper folder. Activate the Python venv:
```
\venv\Scripts\activate
```

OR

You can just install the packages required by:
```
pip install -r requirements.txt
```

4. Choose the difficulty setting in main menu to start the game.
5. Gameplay Controls:
   1. Left-Click: Uncover a cell
   2. Right-Click: Flag a cell

## 3. Requirements
1. Single player game.
   > The player can run the game by following the instructions in the **2. Instructions** and start their game.
3. Computer will randomly choose squares to place the bombs.
   > This is done by the algorithm method "___randomMinePos_" located in "_board.py_'s". Number of bombs and size of the grid are decided when the difficulty is chosen in the main menu. 
   > 
   > Difficulties:
              Easy (9x9), 10 mines ||
              Intermediate (16x16), 40 mines ||
              Hard (22x22), 99 mines.
   >
   > More details can be found in that method and in the files.
   
4. If the grid is a safe one, it should show the number of bombs in its neighbouring squares.
   > If the grid is a safe one, the "__board.py__" method "__handleClickEvent()__" which maintains the logic behind the game checks if there are nearby bombs. If there is 0 bombs around, it checks for the neighbor cells to see if they have any bombs around them. If not, it triggers a click event on that cell. This way, player can uncover multiple cells around the cells they clicked if they are all safe and has no bombs nearby.
   
6. If the player loses the game by pressing on a bomb, then the new game should start with the same grid. (same bombs)
   > If the player uncovers a cell which turns out to be a bomb, "__handleClickEvent()__" sets the game's status as -1 which means loss, and the tick loop in game.py detects this change and stops the game for a while. After the stop, it runs the "__reset()__" method in "__board.py__", which resets the board and all cells back to their initial state with the same bomb placements.
    
8. Until the player wants to quit, they should be able to continue with a new game.
   > If the player wins, a new board is set out for them in the same difficulty with a different bomb placement.
   
10. Flagging a square as a bomb is optional. You can skip this feature if you would like. (As long as the player opens all the squares without a bomb, the player wins the game)
    > The player can flag a sus bomb cell and they can't click on it unless they de-flag it. The win condition for the game is set in the "__board.py__" in "__handleClickEvent()__" as: "self.numUncoveredCells + self.mineCount == self.cellCount". 

## 4. Demonstration
This section provides a video demonstration for the MineSweeper.

https://user-images.githubusercontent.com/19250325/174346559-f391fbd8-8ca2-49bf-b3ea-4ebb204b953d.mp4

