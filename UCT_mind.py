import random
from math import sqrt, log


def think(state):
    me = state.get_whose_turn()
    return UCT(state,25, True)

class Node:
    def __init__(self, move = None, parent = None, state = None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMove = state.get_moves()
        self.playerJustMoved = state.get_player_just_moved()
        #This is a missing part need to add in later!!! self.playerJustMoved = state.


    def UCTselectChild(self):
        s = max(self.childNodes,key=lambda c: float(c.wins) / float(c.visits) + sqrt(2 * log(float(self.visits)) / float(c.visits)))
        return s


    def AddChild(self,m,s):
        n  = Node(move= m, parent = self, state = s)
        self.untriedMove.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self,result):
        self.visits = self.visits + 1
        self.wins += result

    def __repr__(self):
        return "[M: " + str(self.move) + " W/V: " + str(self.wins) + " / " + str(self.visits) + " U: " + str(self.untriedMove) + "]"

    def TreeToString(self,indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
            s += c.TreeToString(indent+1)
        return s

    def IndentString(self,indent):
        s = "\n"
        for i in range(1, indent+1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
            s += str(c) + "\n"
        return s


def UCT(rootstate, maxIter, verbose = False):
    rootnode = Node(state = rootstate)

    for i in range(maxIter):
        node = rootnode
        state = rootstate.copy()

        while node.untriedMove == [] and node.childNodes != []:
            node = node.UCTselectChild()
            state.apply_move(node.move)

        if node.untriedMove != []:
            m = random.choice(node.untriedMove)
            state.apply_move(m)
            node = node.AddChild(m,state)

        while state.get_moves() != []:
            state.apply_move(random.choice(state.get_moves()))

        me = state.get_whose_turn()
        player = state.player_just_moved
        scores = state.get_score(player)
        while node != None:
            #node.Update(scores(node.playerJustMoved))
            node.Update(scores)
            node = node.parentNode

    if(True): print (rootnode.TreeToString(0))
    print("Final Move is: " + str(max(rootnode.childNodes, key=lambda  c:c.wins).move))
    return max(rootnode.childNodes, key=lambda  c:c.visits).move
