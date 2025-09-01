#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the tic-tac-toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.
    Return True if a player has won, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the board is full (no empty spaces left).
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_coordinate(prompt):
    """
    Prompt the user for a valid coordinate (0, 1, or 2).
    Repeat until a valid integer within range is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    Players alternate turns until there is a winner or the board is full (tie).
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row = get_valid_coordinate(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_coordinate(f"Enter column (0, 1, or 2) for player {player}: ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
