## hits ranking algorithm
class node():
    def __init__(self,name):
        self.name=name
        self.friend=[]
        self.hubScore=1
        self.authScore=1

## to add all the nodes to which this one points to and store that in
## the array called friend
    def referTo(self,friend):
        append(self.friend,friend)
        return self

## add to the hub score of the node given another node
    def addHubScore(self,node):
        self.hubScore=self.hubScore+node.authScore
        return
## add to the authority score of the node given another node
    def addAuthscore(self,node):
        self.authScore=self.authScore+node.hubScore
        return

## returns the list of those nodes which are refered to by this node
    def referList(self):
        return self.friend

## return the name of the node
    def __string__():
        return self.name

## sorts the array in terms of hits rankging.
def sort_rank():
    return

## calculates rank of each node based on the hits ranking algor
## rithm.
def cal_rank():
    return

## takes input from a text file and returns an array of classes 
## which represent a graph
def readinput():
    return

## takes a graph in the form of array as input, calculates the 
## hits rank, sorts and returns the sorted array.
def rankHits():
    cal_rank()
    sort_rank()
    return

## function reads in the input from a file and prints out the 
## ranked pages
def main():
    #list of sites is an array that stores instances of site class
    #function reads the intput.
    listOfsites=readinput()
    for j in range(len(listOfsites)):
        listOfsites=rankHits(listOfsites)

    print listOfsite   
    return

main()
