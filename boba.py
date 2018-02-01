import random

def think(state):
    me = state.get_whose_turn()
    moves = state.get_moves()
    bestMove = 0
    bestScore = 0
    for i in range(len(moves)):
        tempState = state.copy();
        tempState.apply_move(moves[i])
        score = tempState.get_score(me)
        score = score + random.uniform(0,1)
        if(score > bestScore):
            bestScore = score
            bestMove = i
    return moves[bestMove]