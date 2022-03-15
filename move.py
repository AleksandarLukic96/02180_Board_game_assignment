import rules


def move(pits, chosenPit, player):
    # Function for making a move on board defined by pits.
    # Which move is defined by chosenPit, an interger in the range
    # 0-5 with numbering from left to right for both sides when the board is seen with player 1 side on top
    # Which player is making the move is given by the input player,  which should be either 1 or 2
    #
    # Returns pits, the new pits after the move, and flag, which is -1 if the move is impossible, i.e. an empty pit
    # is chosen, 0 if move is done and it's the next players turn, and 1 if the same player gets another turn, because
    # the last marble ended in their home pile
    if player == 1:
        chosenPit = chosenPit + (12 - 2 * chosenPit)

    if pits[chosenPit] < 1:
        return pits, -1

    chosenPitPile = pits[chosenPit]
    pits[chosenPit] = 0

    followingPit = chosenPit

    while chosenPitPile > 0:
        followingPit = (followingPit + 1) % 14
        # Skip opponents endpit
        if player == 1 and followingPit == 6:
            followingPit = 7
        if player == 2 and followingPit == 13:
            followingPit = 0
        # Update pits and moving pit pile
        pits[followingPit] = pits[followingPit] + 1
        chosenPitPile -= 1

    # Check on last stone put in pit
    lastPit = followingPit
    if rules.land_in_empty(lastPit, pits) and rules.land_on_own_side(True if player == 1 else False, lastPit):
        pits = rules.capture_opposite(lastPit, pits)

    # Total stones left on each side
    player1StonesLeft = sum(pits[7:13])
    player2StonesLeft = sum(pits[0:6])


    # Winning condition:
    if player1StonesLeft == 0 or player2StonesLeft == 0:
        # Moving the final stones
        pits[0:6] = [0, 0, 0, 0, 0, 0]
        pits[6] = pits[6] + player2StonesLeft
        pits[7:13] = [0, 0, 0, 0, 0, 0]
        pits[13] = pits[13] + player1StonesLeft
        return pits, 0

    if (player == 1 and lastPit == 13) or (player == 2 and lastPit == 6):
        return pits, 1
    return pits, 0
