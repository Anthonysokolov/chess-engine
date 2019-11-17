import chess
import random
from engine import Engine

# TO DO
# Choose move fxn
# End game function to display winner / conditions
# Detect threats and potential attacs
# Detect checkmates


def make_move(board, move):
    '''
    Excecutes a command for a move and updates the board
    Returns bool indicating if operation was successful or not
    '''
    try:
        board.push(move)
    except AttributeError:
        try:
            board.push_san(move)
        except ValueError:
            return False
    return True




def engine_turn(board, engine):
    '''
    Function for engine's turn
    Chooses and move and updates the board
    '''
    move = engine.choose_move(board)
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
    '''
    Main function to play a game against the engine
    Currently: User will always play white
    '''
    move_count = 0
    board = chess.Board()
    engine = Engine()
    print(board)

    while True:
        if not board.is_game_over():
            if move_count % 2 == 0:
                user_turn(board)
            else:
                engine_turn(board, engine)
            move_count += 1
        else:
            # TODO add endgame function
            print("GAME OVER")
            break


play_game()
