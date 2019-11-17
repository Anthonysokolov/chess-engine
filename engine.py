'''
File for chess engine class
Includes functions for all decision making processes
'''
import random
import chess

class Engine:
    def __init__(self):
        self.color = 1
        self.opcolor = 0

    def choose_move(self, board):
        '''
        Function for engine to choose a move
        Returns move to be made
        Make random move
        '''
        moves = [move for move in board.legal_moves]
        attacks = self.attacking_moves(board, moves)

        if attacks:
            return random.choice(attacks)
        return random.choice(moves)

    def attacking_moves(self, board, moves):
        '''
        Returns list of attacking moves
        '''
        out = []
        for m in moves:
            if 'x' in board.san(m):
                out.append(m)
        return out
