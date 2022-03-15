# o---------------------------------------o
# |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
# | 13 |----|----|----|----|----|----|  6 |
# |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
# o---------------------------------------o
def evaluation(pits, player):
    # Check if state is terminal
    if sum(pits[0:6]) + sum(pits[7:13]) == 0:
        if pits[13] > pits[6]:
            return 1000
        elif pits[13] < pits[6]:
            return -1000
        else:
            return 0
    # Counts number of stones each player can put directly in home pile or steal
    player1Home = 0
    player1Steal = 0
    player2Home = 0
    player2Steal = 0
    if player == 1:
        for i in range(12, 6, -1):
            if (pits[i] % 14) == 13 - i:
                player1Home += 1
            if i + pits[i] < 13 and pits[i + pits[i]] == 0:
                pit = i + pits[i]
                player1Steal += 1 + pits[(pit+2*(12-pit)) % 13]
        return player1Home + player1Steal + pits[13] - pits[6]
    elif player == 2:
        for i in range(5, -1, -1):
            if (pits[i] % 14) == 6 - i:
                player2Home += 1
            if i + pits[i] < 6 and pits[i + pits[i]] == 0:
                pit = i + pits[i]
                player2Steal += 1 + pits[12-pit]
        return -(player2Home + player2Steal + pits[6] - pits[13])
    #return player1Home + player1Steal + pits[13]  - (5*player2Home + player2Steal + pits[6] + 0.5*sum(pits[0:6]))
    #return player1Home + player1Steal + pits[13] + 0.1 * sum(pits[7:13]) - 3*(48-sum(pits[7:13]) - sum(pits[0:6]))/48*pits[7:13].count(0) - (player2Home+player2Steal+
    #             pits[6] + 0.1 * sum(pits[0:6])  - 3*(48-sum(pits[7:13]) - sum(pits[0:6]))/48*pits[0:6].count(0))
