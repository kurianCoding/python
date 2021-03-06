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
   
   j,t=row,col
   # if there is a queen diagonally left of it in the current row
   # and column
   while(j>0&&t>0):
       if broad[j][t]==True:
           return False
        j--,t--
   # if there is queen in upper diagonal of this current row
   # and column
   x,y=0,0
   while(x<0&&y>0):
       if broad[x][y]==True:
           return False
