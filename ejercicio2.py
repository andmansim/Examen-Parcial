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
