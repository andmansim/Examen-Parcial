board = []
"""
board = [[R,G , G], 
        [ ,R, R], 
        [G , ,]]
"""
green_rook = ((0,1), (0,2), (2,0))
red_rook = ((0,0), (1,1), (1,2))

def boardcreation():
    line = []
    for i in range(0,3):
        for j in range (0,3):
            if tuple([i,j]) in green_rook:
               line.append("G") 
            elif tuple([i,j]) in red_rook:
                line.append("R")
            else:
                line.append(" ")
        board.append(line)
        line = []
        
boardcreation()

for x in board:
    print("  ".join(x))

# fichero
f = open('HackerChess.txt', 'w')
f.write("HackerChess" + '\n')
for x in range (0,3):
    for y in range(0,3):
        if y == 2:
            f.write(str(board[x][y] + '\n'))
        else:
            f.write(str(board[x][y] + '\t'))
f.close()

print("Player 1 are the red rooks and player 2 the green ones.")
print("Player 1: choose the rook that you want to move. By saying the line and column where it is, remember that the lines and columns go from 0 to 2")
print("Line of the piece:")
player1_line = int(input())
print("Column of the piece:")
player1_column = int(input())
print("New line of the piece:")
player1_new_line = int(input())


if player1_column == 0:
    y = 0
    board[player1_new_line][y] = board[player1_line][y]
    board[player1_line][y] = " "
elif player1_column == 1:
    y = 1
    board[player1_new_line][y] = board[player1_line][y]
    board[player1_line][y] = " "
elif player1_column == 2:
    y = 2
    board[player1_new_line][y] = board[player1_line][y]
    board[player1_line][y] = " "
for x in board:
    print(" ".join(x))
        