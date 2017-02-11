## the program identifies the minimum number of groups from the list of heights of people in the queue.
## since people in a group are nessecarily standing in (weak)increasing order it can be said that there are two groups when a shorter person is 
## standing behind a taller guy.

## function which takes th input
## this code takes in the number of persons in queue N and returns that as an integer array
def getInput():
    number=int(raw_input())
    line=raw_input().split(" ")
    lineN=[]
    for i in range(number):
        lineN.append(int(line[i]))

    return lineN

## function to parse the input and return the number of instances of decreasing order
## this function takes in an array and returns the number of instances of decreasing height
def countDecreasing(array):
    count=0
    for j in range (len(array)-1):
        if(array[j]>array[j+1]):
            count=count+1
        else:
            continue
        
    return count
array=getInput()
count=countDecreasing(array)
print(count+1)
