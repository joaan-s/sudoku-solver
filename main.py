
"""
This is an auxiliar file that will be removed
by implementing it into solver.py
"""
from aux  import *

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

boxes = boxing(board)
changed_cells = []
for row in range(len(boxes)):
    for col in range(len(boxes[row])):
        if board[row][col] == 0:
            ident = 9*row + col
            changed_cells.append([row, col, 0, ident])
"""
for cells in changed_cells:
    if try_number(board, cells[0], cells[1]):
        board[cells[0]][cells[1]] = try_number(board, cells[0], cells[1])
    else:
        break
"""
# Lo de ahora itera los pasos 1, 2, 3, 4 y cuando llega a una contradiccion
# se detiene

# print(changed_cells[49][0])

n = len(changed_cells)
i = 0
while i < n:
    row = changed_cells[i][0]
    col = changed_cells[i][1]
    if try_number(board, row, col):
        board[row][col] = try_number(board, row, col)
        changed_cells[i][2] = try_number(board, row, col)
        i += 1
    else:
        board[row][col] = 0
        changed_cells[i][2] = 0
        i -= 1

print(i)
print(board)