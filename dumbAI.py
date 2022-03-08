def nextMove(pits):
    maxPit = 5
    for i in range(5, -1, -1):
        if pits[i] == 6 - i:
            return i
        elif pits[i] > pits[maxPit]:
            maxPit = i
    return maxPit