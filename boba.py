import random
from queue import Queue
import numpy as np

def think(state):
    Q = Queue()
    list = []
    scoreList = Queue()
    me = state.get_whose_turn()
    moves = state.get_moves()
    rootState = state.copy()

    if(len(moves) == 1):
        return  moves[0]
    best_score = best_move = 0
    for i in range(len(moves)):
        Q.put(rootState.copy().apply_move(moves[i]))
        move_score = 0
        while not Q.empty():
            temp_state = Q.get()
            sub_moves = temp_state.get_moves()
            local_score = local_bestMove = 0
            for j in range(len(sub_moves)):
                newState = temp_state.copy()
                newState.apply_move(sub_moves[j])
                scr = newState.get_score(me)
                if(newState.get_whose_turn() != me):
                    if(scr < local_score):
                        local_score = scr
                        local_bestMove = j
                else:
                    if(scr > local_score):
                        local_score = scr
                        local_bestMove = j
            move_score = move_score + local_score
            state1 = temp_state.copy()
            state1.apply_move(sub_moves[local_bestMove])
            if(not state1.is_terminal()):
                Q.put(state1)
        list.append(move_score)

    targetIndex = list.index(max(list))



    return moves[targetIndex]