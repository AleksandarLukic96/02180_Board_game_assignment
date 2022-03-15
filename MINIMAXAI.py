import math
from move import move


class State:
    def __init__(self, board, boolean):
        self.boardState = board.copy()
        self.MAX = boolean
        if self.MAX:
            self.actions = [12 - i for i in range(7, 13) if self.boardState[i] > 0]
        else:
            self.actions = [i for i in range(6) if self.boardState[i] > 0]


def terminal_test(state):

    return state.boardState[6] + state.boardState[13] == 48 or state.actions == []


def utility(state):
    return state.boardState[13] - state.boardState[6]


def max_value(state, d, max_d):
    if terminal_test(state) or d > max_d:
        return utility(state), None

    v = -100
    amove = None
    for a in state.actions:
        result, flag = move(state.boardState.copy(), a, 1)
        if flag == 1:
            v2, _ = max_value(State(result, True), d, max_d)
        else:
            v2, _ = min_value(State(result, False), d + 1, max_d)
        #print(f"in maxvalue: v = {v}, v2 = {v2}")
        if v2 > v:
            v = v2
            amove = a
    return v, amove


def min_value(state, d, max_d):
    if terminal_test(state) or d > max_d:
        return utility(state), None

    v = 100
    amove = None
    for a in state.actions:
        result, flag = move(state.boardState.copy(), a, 2)
        if flag == 1:
            v2, _ = min_value(State(result, False), d, max_d)
        else:
            v2, _ = max_value(State(result, True), d + 1, max_d)
        if v2 < v:
            v = v2
            amove = a

    return v, amove


def minimax_decision(state, d):
    if state.MAX:
        _, a = max_value(state, 0, d)
    else:
        _, a = min_value(state, 0, d)

    return a



def minimaxMove(d, pits, player):
    if player == 1:
        move = minimax_decision(State(pits, True), d)
    else:
        move = minimax_decision(State(pits, False), d)
    return move
# o---------------------------------------o
# |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
# | 13 |----|----|----|----|----|----|  6 |
# |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
# o---------------------------------------o
