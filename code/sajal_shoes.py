## this is a program that will take in an 
## array of positive integers and divide them in pairs
## it tries to make the maximum number of pairs from 
## the given set of integers

## parses through an array of integers and counts the maximum 
## number of times the number occurs
## it returns an array whose index is the number 
## and value is the number of times that number is
## repeated
def countRepetition(array):
    tArray=array
    repeat={}
    while tArray:
        temp=tArray[0]
        tArray.remove(temp)
        count=1
        while temp in tArray:
            count=count+1
            tArray.remove(temp)
            repeat[temp]=count

    return repeat  

## a function which takes a map as input and divides each entry of the
## map by a number. It returns and integer with is the sum of all the
## quotietns of that division

def pairUp(mapped,pair):
    total=0
    for i in mapped:
        total=total+mapped[i]/pair

    return total


def getInLine(string):
    array_of_chars=string.split(" ")
    return array_of_chars

tests=int(raw_input)
for j in range(tests):
    string=raw_input()
    array_for_count=getInLine(string)
    key_value_count=countRepetition(array_for_count)
    pairs=pairUp(key_value_count,2)
    print pairs
