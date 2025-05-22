import random

generic_board = []
row = []
board_size = 10
for i in range(board_size):
    row.append("X")
for i in range(board_size):
    generic_board.append(row)


def drawBoard(board, draw = True) -> list:
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
        
    if draw:
        print(canvas)
    else:
        return canvas.split("\n")
        
    return []

def draw2boards(b1 : list, b2 : list):
    board1 = drawBoard(b1, False)
    board2 = drawBoard(b2, False)
    result = ""
    spacer = "    "
    for i in range(len(board1)):
       result += board1[i-1] + spacer + board2[i-1] + "\n"

    print(result)

draw2boards(generic_board, generic_board)

