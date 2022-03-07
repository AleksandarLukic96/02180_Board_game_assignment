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

# Value to keep game going
playing = True

# Player 1 = True, Player 2 = False
player = True

# EventHandler
eventCode = 0

# Welcome message - initialised message from https://ascii.co.uk/art/mancala
message = "                                 _       \n                                | |      \n _ __ ___   __ _ _ __   ___ __ _| | __ _ \n| '_ ` _ \ / _` | '_ \ / __/ _` | |/ _` |\n| | | | | | (_| | | | | (_| (_| | | (_| |\n|_| |_| |_|\__,_|_| |_|\___\__,_|_|\__,_|\n"

# Pits to hold stones and the two players end pits
pits = [4, 4, 4, 4, 4, 1, 0, # Player 2 in index 0 to 6
        0, 0, 0, 0, 0, 1, 0] # Player 1 in index 7 to 13
# o---------------------------------------o
# |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
# | 13 |----|----|----|----|----|----|  6 |
# |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
# o---------------------------------------o

# Valid user inputs
validUserInputs = ['a', 'b', 'c', 'd', 'e', 'f']

# Just a test:
#print(validUserInputs.index('e'))

# Game loop
while(playing):

    # Print potential error message
    print(message)
    if player:
        print("Player 1:\n")
    else:
        print("Player 2:\n")

    # Print instructions for Player 1:
    if(player == True):
        print("        a    b    c    d    e    f")

    drawGame.draw_game(pits)

    # Print instructions for Player 2:
    if(player == False):
        print("        a    b    c    d    e    f")

    # Read user input from terminal
    userInput = input()

    # Handle user inputs
    # Quit game
    if userInput == "q":
        print("Quitting the game... \nThanks for playing!")
        playing = False
        break
    # Valid inputs
    elif userInput in validUserInputs:
        chosenPit = 0
        if(player == True):
            if userInput == 'f':
                chosenPit = 7
            elif userInput == 'e':
                chosenPit = 8
            elif userInput == 'd':
                chosenPit = 9
            elif userInput == 'c':
                chosenPit = 10
            elif userInput == 'b':
                chosenPit = 11
            elif userInput == 'a':
                chosenPit = 12
        elif(player == False):
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

    # Check if chosen pit is empty
    if pits[chosenPit] > 0:
            chosenPitPile = pits[chosenPit]
            pits[chosenPit] = 0
            message = ""
            #player = not(player)
    else:
       message = "The chosen pit was empty! Try again..."

    # Move stones from chosen pit to following pits
    followingPit = chosenPit + 1
    while(chosenPitPile > 0):
        # Check if pit is out of bounds
        if(followingPit > 13):
            followingPit = 0
        # Skip oponents endpit
        if(player == True and followingPit == 6):
            followingPit = 7
        if(player == False and followingPit == 13):
            followingPit = 0
        # Update pits and moving pit pile
        pits[followingPit] = pits[followingPit] + 1
        chosenPitPile = chosenPitPile - 1
        # Stops incrementation when pile size is 0
        if(chosenPitPile > 0):
           followingPit = followingPit + 1

    # If last stone ends on the players end pit, that player gets another turn
    if(player == True and followingPit == 13):
        message = "Last stone ended in Player 1's end pit!"
    elif(player == False and followingPit == 6):
        message = "Last stone ended in Player 2's end pit!"
    else:
        # Changes player
        player = not(player)

    # Winning condition:
    if ((int(pits[0]) == 0) and (int(pits[1]) == 0) and (int(pits[2]) == 0) and (int(pits[3]) == 0) and (int(pits[4]) == 0) and (int(pits[5]) == 0)) or ((int(pits[7]) == 0) and (int(pits[8]) == 0) and (int(pits[9]) == 0) and (int(pits[10]) == 0) and (int(pits[11]) == 0) and (int(pits[12]) == 0)):
        if(pits[13] > pits[6]):
            print("Player 1 Wins!")
            playing = False
        elif(pits[13] < pits[6]):
            print("Player 2 Wins!")
            playing = False
        else:
            print("It's a tie!")
            playing = False
