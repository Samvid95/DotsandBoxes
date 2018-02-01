def think(state):
    me = state.get_whose_turn()
    moves = state.get_moves()
    return moves[0]
