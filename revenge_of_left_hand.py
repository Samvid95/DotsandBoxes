import random
from DotsandBoxes import  greedo
from math import sqrt, log


def think(state):
    me = state.get_whose_turn()
    return UCT(state,1000, True)

class Node:
    def __init__(self, move = None, parent = None, state = None, last_move = None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMove = state.get_moves()
        self.playerJustMoved = last_move
        #This is a missing part need to add in later!!! self.playerJustMoved = state.


    def UCTselectChild(self):
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + sqrt(2 * log(self.visits,2) / c.visits))[-1]
        return s


    def AddChild(self,m,s,last_move = None):
        n  = Node(move= m, parent = self, state = s,last_move = last_move)
        self.untriedMove.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self,result):
        self.visits = self.visits + 1
        self.wins += result
'''
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
'''

def UCT(rootstate, maxIter, verbose = False):
    rootnode = Node(state = rootstate, last_move= rootstate.get_whose_turn())
    rootnode.visits =1.0

    for i in range(maxIter):
        node = rootnode
        state = rootstate.copy()

        #selection
        while node.untriedMove == [] and node.childNodes != []:
            node = node.UCTselectChild()
            state.apply_move(node.move)

        #Expansion
        if node.untriedMove != []:
            m = random.choice(node.untriedMove)
            turn = state.get_whose_turn()
            state.apply_move(m)
            node = node.AddChild(m,state,last_move=turn)


        while state.get_moves() != []:
            nextMove = greedo.think(state)
            state.apply_move(nextMove)


        while node != None:
            scores = state.get_score(node.playerJustMoved)
            node.Update(scores)
            node = node.parentNode

    #if(True): print (rootnode.TreeToString(0))
    #print("Final Move is: " + str(max(rootnode.childNodes, key=lambda  c:c.wins).move))
    return sorted(rootnode.childNodes, key=lambda c: c.wins / c.visits)[-1].move
