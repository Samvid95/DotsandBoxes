from random import randint

def think(state):
    me = state.get_whose_turn()
    moves = state.get_moves()
    moveNum = (randint(0,(len(moves)-1)))
    return moves[moveNum]