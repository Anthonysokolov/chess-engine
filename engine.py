'''
File for chess engine class
Includes functions for all decision making processes
'''
import random

class Engine:
    def __init__(self):
        pass

    def choose_move(self, board):
        '''
        Function for engine to choose a move
        Returns move to be made
        Make random move
        '''
        moves = [move for move in board.legal_moves]
        return random.choice(moves)
