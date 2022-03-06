
# Value to keep game going
playing = True

# Pits to hold stones and the two players end pits
pits = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    

# Game loop
while(playing):
      
    print(pits)
    
    userInput = input()
    
    # Quit game
    if userInput == "q":
        playing = False
    
    
    


