def nextMove(pits, player):
    # Simple, greedy AI, that chooses next move from pits, assuming to be player given as input 1 or 2.
    # The move is chosen to be the first pile closest to the home pile that ends in the home pile,
    # or if none does, the closest pile to the home pile with the most marbles
    if player == 2:
        maxPit = 5
        for i in range(5, -1, -1):
            if (pits[i] % 14) == 6 - i: # If pit holds enough marbles to end in home pile, also when going round the board
                return i
            elif pits[i] > pits[maxPit]:
                maxPit = i
        return maxPit
    # Considers other half of the board. Also recalculates the output to be between 0-5 to fit with expected input for move
    elif player == 1:
        maxPit = 12
        for i in range(12, 6, -1):
            if (pits[i] % 14) == 13 - i: # If pit holds enough marbles to end in home pile, also when going round the board
                return -i + 12
            elif pits[i] > pits[maxPit]:
                maxPit = i
        return -maxPit + 12