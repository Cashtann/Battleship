import random

board = []
row = []
board_size = 10
for i in range(board_size):
    row.append("X")
for i in range(board_size):
    board.append(row)


def drawBoard():
    size_mult = 1 if board_size < 10 else 2
    canvas = size_mult * " "

    for j in range(board_size):
        canvas += "|" + chr(65+j)

    canvas += "|\n"
    for i in range(board_size):
        canvas += size_mult * "-" + board_size * "|-" + "|\n"
        canvas += str(i+1) + " |" if (i+1) < 10 else str(i+1) + "|"

        for j in range(board_size):
            canvas += board[j][i] + "|"
        canvas += "\n"

    canvas += size_mult * "-" + board_size * "|-" + "|\n"
        

    print(canvas)

drawBoard()



