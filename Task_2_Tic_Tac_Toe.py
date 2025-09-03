""" Tic-Tac-Toe with an AI Agent (Unbeatable using Minimax + Alpha-Beta Pruning) """

import random

# All possible winning combinations (3 rows, 3 cols, 2 diagonals)
WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Columns
    (0, 4, 8), (2, 4, 6)               # Diagonals
]

def print_board(board):
    """Prints the Tic-Tac-Toe board in a 3x3 grid."""

    box = [c if c != " " else str(i + 1) for i, c in enumerate(board)]
    print(f"\n {box[0]} | {box[1]} | {box[2]}")
    print("---+---+---")
    print(f" {box[3]} | {box[4]} | {box[5]}")
    print("---+---+---")
    print(f" {box[6]} | {box[7]} | {box[8]}\n")


def check_winner(board):
    """Checks if someone has won or if it's a draw."""
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Return "X" or "O"

    if " " not in board:
        return "D"  # Draw
    return None  # Game not over

def available_moves(board):
    """Returns list of indexes that are empty."""
    return [i for i, c in enumerate(board) if c == " "]

# -------------------- Minimax Algorithm -------------------- #

def minimax(board, depth, is_maximizing, alpha, beta, ai, human):
    
    winner = check_winner(board)
    if winner is not None:
        # Scoring system
        if winner == ai:
            return 10 - depth
        elif winner == human:
            return depth - 10
        else:
            return 0  # Draw

    if is_maximizing:
        max_eval = -float("inf")
        for move in available_moves(board):
            board[move] = ai
            score = minimax(board, depth + 1, False, alpha, beta, ai, human)
            board[move] = " "
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in available_moves(board):
            board[move] = human
            score = minimax(board, depth + 1, True, alpha, beta, ai, human)
            board[move] = " "
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, ai, human):
    """Finds the best move for the AI using Minimax."""
    best_score = -float("inf")
    move = None
    for i in available_moves(board):
        board[i] = ai
        score = minimax(board, 0, False, -float("inf"), float("inf"), ai, human)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

# -------------------- Main Game Loop -------------------- #

def play_game():
    print("=== Welcome to Tic-Tac-Toe with AI ===")
    board = [" "] * 9

    # Choose boxbols
    human = input("Choose your boxbol (X/O): ").upper()
    ai = "O" if human == "X" else "X"

    # Choose who goes first
    turn = input("Do you want to start first? (yes/no): ").lower()
    human_turn = True if turn == "yes" else False

    print_board(board)

    while True:
        if human_turn:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move, try again.")
                continue
            board[move] = human
        else:
            print("AI is thinking...")
            move = best_move(board, ai, human)
            board[move] = ai
            print(f"AI chooses position {move + 1}")

        print_board(board)

        result = check_winner(board)
        if result is not None:
            if result == "D":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        human_turn = not human_turn


if __name__ == "__main__":
    play_game()
