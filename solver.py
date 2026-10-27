
"""
A board will be a 9-list of 9-lists,
and empty cells are filled with zero's.
"""

"""
Im having problems with OOP, so i'll do it simpler in main.py
when everything works there I'll come back here
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

class Board:
    def __init__(self, board):
        self.board = board

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


    def boxes(board):
        boxes = []
        for i in range(9):
            box = []
            q = i//3
            r = i%3
            for j in range(3):
                for k in range(3):
                    box.append(board[q+j][r+k])
            boxes.append(box)
        return boxes

    def box(board, row, col):
        boxes = board.boxes
        return boxes[row//3+col%3]


    def valid_num(board, row, col, num):
        # Checking rows
        for cells in board[row]:
            if cells == num:
                return False
        # Checking columns
        for i in range(9):
            if board[i][col] == num:
                return False
        # Checking boxes
        for cells in box:
            if cells == num:
                return False
        return True

    """
    def choose_number(board, row, col):
        for num in range(1, 10):
            if valid_num(board, row, col, num):
    """

board = Board(board)
print(board.boxes())