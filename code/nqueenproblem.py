# this is a program in the backtracking algorithm series
# it tries to demonstrate the woring of a typical backtracking
# algorithm. while doing so it solves the problem of placing
# N queens on a table with none of them in the direct line
# of each other
# by kurianck.mail@gmail.com

# a function to check if the current row has any position
# available for placing a queen
def isSafe(board,row,col):
    # if there is a qeen to the left of the current column in 
    # this row then its not safe
    for i in range(col):
        if board[row][i]==True:
            return False
