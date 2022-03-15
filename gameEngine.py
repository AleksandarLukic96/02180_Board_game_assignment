# 02180 Introduction to Artificial Intelligence
# Project: AI to play Mancala / Kalaha
# Technical University of Denmark (DTU)
# March 2022 
# Authors:
#   Aleksandar Lukic  s194066
#   Hjalte Pind       s183811
#   Jacob Hellum      s194021
#   Søren Hinrichsen  s183807

import drawGame
from dumbAI import nextMove as dumbMove
from move import move
from MINIMAXAI import minimaxMove

# Value to keep game going
playing = True

# Player 1 = True, Player 2 = False
player1Turn = True

# EventHandler
eventCode = 0

def startMenu(player):
    # Menu for asking user for integer. If something else than an integer in the valid options is given, returns -1,
    # else returns the integer
    valid_ints = [1, 2, 3]
    print("Player {} plays as:\n 1: Human\n 2: Dumb AI\n 3: Minimax".format(player))
    startChoice = input()
    try:
        int(startChoice)
        if int(startChoice) not in valid_ints:
            print("Not a valid input!")
            return -1
        return int(startChoice)
    except:
        print("Not a valid input!")
        return -1

# Asks if players are humans or Ai, and which AI
startChoice = startMenu(1)
while startChoice == -1:
    startChoice = startMenu(1)

if startChoice == 1:
    player1 = 'Human'
elif startChoice == 2:
    player1 = 'AI'
    AI1Move = dumbMove
elif startChoice == 3:
    player1 = 'AI'
    AI1Move = minimaxMove

startChoice = startMenu(2)
while startChoice == -1:
    startChoice = startMenu(2)

if startChoice == 1:
    player2 = 'Human'
elif startChoice == 2:
    player2 = 'AI'
    AI2Move = dumbMove
elif startChoice == 3:
    player2 = 'AI'
    AI2Move = minimaxMove

# Welcome message - initialised message from https://ascii.co.uk/art/mancala
message = "                                 _       \n                                | |      \n _ __ ___   __ _ _ __   ___ __ _| | __ _ \n| '_ ` _ \ / _` | '_ \ / __/ _` | |/ _` |\n| | | | | | (_| | | | | (_| (_| | | (_| |\n|_| |_| |_|\__,_|_| |_|\___\__,_|_|\__,_|\n"

# Pits to hold stones and the two players end pits
pits = [4, 4, 4, 4, 4, 4, 0,  # Player 2 in index 0 to 6
        4, 4, 4, 4, 4, 4, 0]  # Player 1 in index 7 to 13
# o---------------------------------------o
# |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
# | 13 |----|----|----|----|----|----|  6 |
# |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
# o---------------------------------------o

# Valid user inputs
validUserInputs = ['a', 'b', 'c', 'd', 'e', 'f']

# Just a test:
# print(validUserInputs.index('e'))

# Game loop
while playing:

    # Print potential error message
    print(message)
    if player1Turn:
        print("Player 1:\n")
    else:
        print("Player 2:\n")

    # Print instructions for Player 1:
    if player1Turn and player1 == 'Human':
        print("        a    b    c    d    e    f")
    drawGame.draw_game(pits)

    # Print instructions for Player 2:
    if (not player1Turn) and player2 == 'Human':
        print("        a    b    c    d    e    f")

    # Read user input from terminal
    if (player1Turn and player1 == 'Human') or (not player1Turn and player2 == 'Human'):
        userInput = input()
        # Handle user inputs
        # Quit game
        if userInput == "q":
            print("Quitting the game... \nThanks for playing!")
            playing = False
            break
        # Valid inputs
        elif userInput in validUserInputs:
            if userInput == 'a':
                chosenPit = 0
            elif userInput == 'b':
                chosenPit = 1
            elif userInput == 'c':
                chosenPit = 2
            elif userInput == 'd':
                chosenPit = 3
            elif userInput == 'e':
                chosenPit = 4
            elif userInput == 'f':
                chosenPit = 5
        # Invalid inputs
        else:
            message = "Invalid input, try again..."
            continue
    elif (player1Turn and player1 == 'AI'):
        chosenPit = AI1Move(pits, 1)
    elif (not player1Turn) and player2 == 'AI':
        chosenPit = AI2Move(pits, 2)

    pits, flag = move(pits, chosenPit, 1 if player1Turn else 2)

    if flag == -1:
        message = "The chosen pit was empty! Try again..."
        continue

    # If last stone ends on the players end pit, that player gets another turn
    if player1Turn and flag == 1:
        message = "Last stone ended in Player 1's end pit!"
    elif not player1Turn and flag == 1:
        message = "Last stone ended in Player 2's end pit!"
    else:
        # Changes player
        player1Turn = not player1Turn
        message = ""

    # Total stones left on each side
    player1StonesLeft = sum(pits[7:13])
    player2StonesLeft = sum(pits[0:6])


    # Winning condition:
    if player1StonesLeft == 0 or player2StonesLeft == 0:

        drawGame.draw_game(pits)

        if (pits[13] > pits[6]):
            print("Player 1 Wins!")
        elif (pits[13] < pits[6]):
            print("Player 2 Wins!")
        else:
            print("It's a tie!")
        playing = False
