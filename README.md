# 02180_Board_game_assignment
Git Repository for 02180 Introduction to AI 
Assignment 1 : Board game

## **Game rules of Mancala:** ##
1. The goal of the game is to collect more stones than your oponent by the end of the game.

2. The game board consists of 12 pits, each containing 4 stones at the start of the game, totalling in 48 stones. The 12 pits are split into to rows of 6 pits, one for each player.

3. At the ends of the board, each player have a coorospnding mancala to collect stones into. When stones are put in a mancala they stay there until the game ends.

4. The players take turns picking up the stones from one of their own pits and dividing them one by one into the following pits, moving counter-clockwise. Players can only pick up stones from their own 6 pits and not their mancala.

5. When placing stones in the following pits, should the player get to their own mancala, they get to put a stone in. If there are still more stones left to be placed, the player continue placing stones in the oponents pits moving counter-clockwise. Then, if the player reaches all the way to the oponents mancala, they skip it and continue onto their own side.

6. If the last stone is placed in the players mancala, the player gets to take another turn.

7. If the last stone is placed in an empty pit on the players side, the player can capture this stone along with all the stones in the pit across it on the oponents side and put them all into the players mancala.

8. The game ends when one of the players empty their side. At this point, the oponent get to claim all remaining stones on their side. The winner is the player with most stones in their mancala. 

## **How to play Mancala in terminal:** ##
1. Download the folder from the git-repository: https://github.com/AleksandarLukic96/02180_Board_game_assignment and save it on the computer.

2. Open your choice of terminal, ex. Command Prompt (cmd.exe) and change directory to where you have saved the folder.
```
> cd 02180_Board_game_assignment
```

3. Now run the file _gameEnigine.py_.
```
> gameEnigine.py
```

4. While playing the game board is printed in the terminal showing all the pits and mancalas. Since each player can only pick up stones from their own side, the player can see the letters _a_, _b_, _c_, _d_, _e_ and _f_ either right above or underneath their pits.
<!-- Screenshot from cmd-prompt-->
![](https://github.com/AleksandarLukic96/02180_Board_game_assignment/Images/MancalaTerminal1.JPG)

5. When the player wants to choose a pit, they write in the terminal the coorosponding letter. 

6. If the player writes an invalid input to the terminal, the game will reprompt for a valid input.

## Links ##
Inspiration for the GUI:
https://ascii.co.uk/art/mancala

Playable online game: 
https://www.mathplayground.com/mancala.html
 
