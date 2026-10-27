
"""
This is an auxiliar file that will be removed
by implementing it into solver.py
"""

board = [
    [0, 5, 0, 7, 0, 8, 0, 6, 4],
    [0, 0, 0, 4, 2, 0, 0, 0, 0],
    [0, 0, 6, 5, 1, 0, 0, 2, 0],
    [0, 3, 4, 0, 5, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 2],
    [5, 2, 0, 0, 0, 0, 0, 9, 6],
    [0, 7, 0, 0, 8, 0, 0, 0, 0],
    [3, 1, 0, 0, 0, 5, 2, 0, 8],
    [4, 6, 0, 2, 0, 0, 9, 0, 0]
]


def boxing(board):
    boxes = []
    for i in range(3):
        for l in range(3):
            box = []
            for j in range(3):
                for k in range(3):
                    box.append(board[3*i+j][3*l+k])
            boxes.append(box)
    return boxes

def which_box(boxes, row, col):
    """
    boxes = [0, 1, 2]
            [3, 4, 5]
            [6, 7, 8]
    """
    return boxes[3*(row//3)+col//3]

def find_empty(board):
    # Picks an empty board and findes empty cells ordered
    # by rows and cols.
    # Important row, col go from 0 to 8.
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)
            else:
                return None

def valid_num(board, boxes, row, col, num):
    # Checking rows
    for cells in board[row]:
        if cells == num:
            return False
    # Checking columns
    for i in range(9):
        if board[i][col] == num:
            return False
    # Checking boxes
    box = which_box(boxes, row, col)
    for cells in box:
        if cells == num:
            return False
    return True

boxes = boxing(board)
print(valid_num(board, boxes, 0, 0, 1))

# Continue bby implementing backtracking algorithm