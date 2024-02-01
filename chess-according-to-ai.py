import os
import sys
import chess
import chess.svg

def display_board(board):
    print(chess.svg.board(board=board, lastmove=None, check=None, coordinates=True))

def get_move():
    move = input("Enter your move (e.g. e2e4): ")
    try:
        move = chess.Move.from_uci(move)
        if move in board.legal_moves:
            return move
        else:
            print("Illegal move. Try again.")
            return get_move()
    except ValueError:
        print("Invalid input. Try again.")
        return get_move()

def main():
    board = chess.Board()
    while not board.is_game_over():
        display_board(board)
        move = get_move()
        board.push(move)
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Game over.")
    print(board.result())

if __name__ == "__main__":
    main()