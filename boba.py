import random
from DotsandBoxes import  greedo
from queue import Queue
import numpy as np


ROLLOUTS = 10

def think(state):
    moves = state.get_moves()

    best_move = greedo.think(state)
    best_expectation = float("-inf")

    me = state.get_whose_turn()

    def rollout(state):
        while not state.is_terminal():
            rollout_move = greedo.think(state)
            state.apply_move(rollout_move)
        return state.get_score(me)

    for move in moves:
        total_score = 0.0

        for r in range(ROLLOUTS):
            rollout_state = state.copy()

            rollout_state.apply_move(move)

            total_score += sum([rollout(rollout_state) for i in range(ROLLOUTS)])

        expectation = float(total_score) / ROLLOUTS

        if expectation > best_expectation:
            best_expectation = expectation
            best_move = move

    return best_move