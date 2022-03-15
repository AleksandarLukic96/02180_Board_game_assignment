import math
from move import move
from evaluation import evaluation

class State:
    def __init__(self, board, boolean):
        self.boardState = board.copy()
        self.MAX = boolean
        if self.MAX:
            self.actions = [12 - i for i in range(7, 13) if self.boardState[i] > 0]
        else:
            self.actions = [i for i in range(6) if self.boardState[i] > 0]


def terminal_test(state):

    return state.boardState[6] + state.boardState[13] == 48


def utility(state):
    #return state.boardState[13] - state.boardState[6]
    return evaluation(state.boardState, 1 if state.MAX else 2)

def max_value(state, d, max_d, alpha, beta):
    if terminal_test(state) or d > max_d:
        return utility(state), None

    v = -float('inf')
    for a in state.actions:
        result, flag = move(state.boardState.copy(), a, 1)
        if flag == 1:
            v2, _ = max_value(State(result, True), d, max_d, alpha, beta)
        else:
            v2, _ = min_value(State(result, False), d + 1, max_d, alpha, beta)
        if v2 > v:
            v = v2
            amove = a
            alpha = max(alpha, v)
        if v >= beta:
            return v, amove
    return v, amove


def min_value(state, d, max_d, alpha, beta):
    if terminal_test(state) or d > max_d:
        return utility(state), None

    v = float('inf')
    for a in state.actions:
        result, flag = move(state.boardState.copy(), a, 2)
        if flag == 1:
            v2, _ = min_value(State(result, False), d, max_d, alpha, beta)
        else:
            v2, _ = max_value(State(result, True), d + 1, max_d, alpha, beta)
        if v2 < v:
            v = v2
            amove = a
            beta = min(beta, v)
        if v <= alpha:
            return v, amove
    return v, amove


def minimax_decision(state, d):
    if state.MAX:
        _, a = max_value(state, 0, d, -float('inf'), float('inf'))
    else:
        _, a = min_value(state, 0, d, -float('inf'), float('inf'))

    return a



def alphabetaMove(d, pits, player):
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
