
"""
A board will be a 9-list of 9-lists,
and empty cells are filled with zero's.
"""

def find_empty(board):
    # Picks an empty board and findes empty cells ordered
    # by rows and cols
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)

