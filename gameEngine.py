
# Value to keep game going
playing = True

# Pits to hold stones and the two players end pits
pits = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    

# Game loop
while(playing):
    
    # loop to format number in pits
    i = 0
    for pit in pits:
        if int(pits[i]) < 10:
            pits[i] = " " + str(pits[i])
        else:
            pits[i] = str(pits[i])
        i = i + 1
      
    print(pits)
    
    userInput = input()
    
    # Quit game
    if userInput == "q":
        playing = False
    
    
    


