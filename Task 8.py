def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve_nqueen(board, row + 1, n):
                return True

            board[row] = -1

    return False


n = int(input("Enter number of queens: "))

board = [-1] * n

if solve_nqueen(board, 0, n):
    print("Solution:")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")
