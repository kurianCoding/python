## the program takes in an array of non-negative integers. This
## is subjected to the following process.
## 1. select two consecutive entries of the array
## 2. substract 1 from both of them.
## if a  finite itration of this process can give us an array of zeros
## then then the program prints YES and otherwise NO

def getInput():
    rawin=raw_input().split(" ")
    array=[]
    for i in range(len(rawin)):
        array.append(int(rawin[i]))

    return array

## this function takes in an array of integers and a boolean. depending
## on whether the boolean equals a true or false it returns the sum of odd
## or even terms
def getSumOf(oddOrEven,array):
    if (oddOrEven==True):
        start=1
    else:
        start=0
    summation=0
    for i in xrange(start,len(array)-1,2):
        summation=summation+array[i]
    if summation==0:
        summation=array[start]
    return summation
array=getInput()
Even=True
Odd=False
if(getSumOf(Even,array)==getSumOf(Odd,array)):
    print "YES"
else:
    print "NO"
