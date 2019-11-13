import chess
import random

# TO DO
# Choose move fxn
# Make move fxn and handle all cases
# End game on checkmate
# Two sides


def make_move(board, move):
    try:
        board.push(move)
    except AttributeError:
        try:
            board.push_san(move)
        except ValueError:
            return False
    return True

def choose_move(board):
    '''
    Function for engine to choose a move
    Returns move to be made
    Make random move
    '''
    moves = [move for move in board.legal_moves]
    return random.choice(moves)


def engine_turn(board):
    '''
    Function for engine's turn
    Chooses and move and updates the board
    '''
    move = choose_move(board)
    make_move(board, move)
    print('***************\n')
    print("ENGINE MADE THE MOVE " + str(move))
    print(board)


def user_turn(board):
    '''
    Function for user's turn
    Gets input for move and updates board
    '''
    print(board.legal_moves) # Display available moves

    # Get move as input string
    move = input("Move: ")
    # Handle invalid moves
    while not make_move(board, move):
        print("INVALID MOVE! ENTER ANOTHER")
        move = input("Move: ")

    print('***************\n')
    print("YOU MADE THE MOVE " + str(move))
    print(board)


def play_game():
    board = chess.Board()
    print(board)

    while True:
        user_turn(board)
        engine_turn(board)


play_game()
