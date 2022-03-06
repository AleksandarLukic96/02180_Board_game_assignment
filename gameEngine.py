
# Value to keep game going
playing = True

# Pits to hold stones and the two players end pits
pits = [0, 4, 4, 4, 4, 4, 4, # Player 1 in index 0 to 6 
        4, 4, 4, 4, 4, 4, 0] # Player 2 in index 7 to 13
    

# Game loop
while(playing):
    
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
    print("o----------------------------------o")
        
    # Print Player 1:  
    playerOneSide = "|    | "
    for i in range(1, 6):
        playerOneSide = playerOneSide + str(pits[i]) + " | "
    playerOneSide = playerOneSide + "   |"
    print(playerOneSide)
    
    # Print player pits and seperation between sides
    print("| " + pits[0] + " |----|----|----|----|----| " + pits[13] + " |")
    
    # Print Player 2:  
    playerTwoSide = "|    | "
    for i in range(7, 12):
        playerTwoSide = playerTwoSide + str(pits[i]) + " | "
    playerTwoSide = playerTwoSide + "   |"
    print(playerTwoSide)
    
    # Print bottom border of board
    print("o----------------------------------o")
    
    userInput = input()
    
    # Quit game
    if userInput == "q":
        playing = False
    
    
    


