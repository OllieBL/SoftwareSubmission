import numpy as np

board = np.array([
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
])
turn = 0
while True:
    turn += 1
    boardChangex = int(input('row'))
    boardChangey = int(input('column'))
    if turn%2 == 0:
        board[boardChangex][boardChangey] = 'X'
    else:
        board[boardChangex][boardChangey] = 'O'
    print(board)