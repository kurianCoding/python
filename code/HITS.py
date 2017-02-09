##hits ranking algorithm

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
