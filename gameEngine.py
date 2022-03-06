# 02180 Introduction to Artificial Intelligence
# Project: AI to play Mancala / Kalaha
# Technical University of Denmark (DTU)
# March 2022 
# Authors:
#   Aleksandar Lukic  s194066
#   Hjalte Pind       s183811
#   Jacob Hellum      s194021
#   Søren Hinrichsen  s183807

# Value to keep game going
playing = True

# Player 1 = True, Player 2 = False
player = True

# Welcome message
message = "Welcome to Mancala!\n"

# Pits to hold stones and the two players end pits
pits = [0, 1, 2, 3, 4, 5, 6, # Player 2 in index 0 to 6 
        7, 8, 9, 10, 11, 12, 13] # Player 1 in index 7 to 13
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
    
    print(message)
    
    if player:
        print("Player 1: ")
    else:
        print("Player 2: ")
    
    
    # loop to format number in pits
    i = 0
    for pit in pits:
        pits[i] = int(pits[i])
        if int(pits[i]) < 10:
            pits[i] = " " + str(pits[i])
        else:
            pits[i] = str(pits[i])
        i = i + 1
    
    # Print top border of board
    print("o---------------------------------------o")
        
    # Print Player 1:  
    playerOneSide = "|    | "
    for i in range(12, 6, -1):
        playerOneSide = playerOneSide + str(pits[i]) + " | "
    playerOneSide = playerOneSide + "   |"
    print(playerOneSide)
    
    # Print player pits and seperation between sides
    print("| " + pits[13] + " |----|----|----|----|----|----| " + pits[6] + " |")
    
    # Print Player 2:  
    playerTwoSide = "|    | "
    for i in range(0, 6):
        playerTwoSide = playerTwoSide + str(pits[i]) + " | "
    playerTwoSide = playerTwoSide + "   |"
    print(playerTwoSide)
    
    # Print bottom border of board
    print("o---------------------------------------o")
    
    # Read user input from terminal
    userInput = input()
    
    # Handle user inputs
    # Quit game
    if userInput == "q": 
        print("Quitting the game... \nThanks for playing!")
        playing = False
    # Valid inputs
    elif userInput in validUserInputs: 
        message = ""
        player = not(player)
    # Invalid inputs
    else: 
        message = "Invalid input, try again..."
    
    