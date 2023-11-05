def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0

    return False

# Initialize the board with 0's
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

# Place the first Queen at (0, 0)
row=int(input("Enter the row to place the queen"))
board[row][0] = 1

# Solve the 8-Queens problem
if solve_n_queens(board, 1):
    print("Solution found:")
    print_board(board)
else:
    print("No solution exists")
    print_board(board)
