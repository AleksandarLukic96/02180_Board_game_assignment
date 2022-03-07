
def draw_game(pits):
    # loop to format number in pits
    print("o---------------------------------------o")

    # Print Player 1 side:
    print("|    | ", end='')
    for i in range(12, 6, -1):
         print(f"{pits[i]:2} | ",end='')
    print("   |")

    # Print player pits and seperation between sides
    print(f"| {pits[13]:2} |----|----|----|----|----|----| {pits[6]:2} |")

    # Print Player 2 side:
    print("|    | ", end='')
    for i in range(0, 6):
        print(f"{pits[i]:2} | ", end='')
    print("   |")

    # Print bottom border of board
    print("o---------------------------------------o")

