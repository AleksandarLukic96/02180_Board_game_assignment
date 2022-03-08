# Player 1:
# o---------------------------------------o
# |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
# | 13 |----|----|----|----|----|----|  6 |
# |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
# o---------------------------------------o
# Player 2:

def land_in_empty(lastPit, pits):
    return pits[lastPit] == 1


def land_on_own_side(player1, lastPit):
    player2 = not player1
    return (player1 and lastPit in [7, 8, 9, 10, 11, 12]) or (player2 and lastPit in [0, 1, 2, 3, 4, 5])


def capture_opposite(lastPit, pits):

    for (p1, p2) in zip([0, 1, 2, 3, 4, 5], [12, 11, 10, 9, 8, 7]):
        # Player1 side
        if lastPit == p1 and pits[p2] != 0:
            pits[6] = pits[6] + pits[p1] + pits[p2]
            pits[p1] = 0
            pits[p2] = 0

        elif lastPit == p2 and pits[p1] != 0:
            pits[13] = pits[13] + pits[p1] + pits[p2]
            pits[p1] = 0
            pits[p2] = 0

    return pits
