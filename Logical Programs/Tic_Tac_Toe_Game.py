import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def user_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column between 0 and 2.")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            break

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        user_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        computer_move(board)
        print("Computer's move:")
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

play_game()
