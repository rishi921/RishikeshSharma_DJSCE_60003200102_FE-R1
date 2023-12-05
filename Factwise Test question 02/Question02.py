import time

def solve(board):
    find = find_empty(board)
    if not find: 
        return board 
    
    row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = str(i)

            if solve(board):
                return board

            board[row][col] = '.'
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return (i, j)

    return None

def valid(board, num, pos):
    # Checking Rows
    for i in range(9):    
        if board[pos[0]][i] == str(num) and i != pos[1]:
            return False

    # Checking columns
    for i in range(9):
        if board[i][pos[1]] == str(num) and i != pos[0]:
            return False

    box_row_start = pos[0] // 3
    box_col_start = pos[1] // 3

    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == str(num) and (box_row_start + i, box_col_start + j) != pos:
                return False
    return True  

    board = [
        ["5","3",".",".",".",".",".",".","."],
        ["6",".",".",".","1","9","5","4","."],
        [".","9","8",".",".",".",".",".","."],
        ["8",".",".",".",".","3",".",".","."],
        [".",".",".",".",".",".",".",".","1"],
        ["7",".",".",".",".","2",".",".","."],
        [".","6",".",".",".",".",".","2","8"],
        [".",".",".",".",".",4,"1","9",".",".","5"],
        [".",".",".",".",8,".",".",".",7,"9"]
    ]
    solution = solve(board)
    print(solution)