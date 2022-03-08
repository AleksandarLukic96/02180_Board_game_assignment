def nextMove(pits):
    # Simple, greedy AI, that chooses next move from pits, assuming to be player 2. The move is chosen to be the
    # first pile closest to the home pile that ends in the home pile, or if none does, the closest pile to the home
    # pile with the most marbles
    maxPit = 5
    for i in range(5, -1, -1):
        if (pits[i] % 14) == 6 - i:
            return i
        elif pits[i] > pits[maxPit]:
            maxPit = i
    return maxPit