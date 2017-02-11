## this program scans an array containing 
## only zeros and ones.
## It executes two type of queries on this array.
## 1. given the index it changes the value stored 
## in that index from a zero to one or vice versa
## 2. given two indices with the first one less than
## the second it attempts to predict if the binary
## number represented by the substring of the array 
## formed by values in and between the two indices
## is even or ODD


def getInput(array_length):
    input_string=raw_input().split(" ")
    input_array=[]
    for i in range(array_length):
        input_array.append(int(input_string[i]))

    return input_array

## is a function which takes in an integer query and 
## an integer array(on which operations are done)
## it takes from the prompt queries and swithces th
## em according to the type of queries they belong 
## to.
def getQueries(query,array):
    for i in range(query):
        querystring=raw_input().split(" ")
        if(querystring[0]=='0'):
            result="EVEN" if getNumber(int(querystring[1])-1,int(querystring[2])-1,array) else "ODD"
            print result
        else:
            array=flipValue(int(querystring[1])-1,array)

    return




    
## this function takes an integer and an integer
## array as the input.It flips the value stored
## in the index mod 2.
def flipValue(index,array):
    array[index]=(array[index]+1)%2
    return array


## this function takes the starting index, ending
## index and an array of numbers. It returns true if
## the number formed by values in the subarray btw the
## indices is even and returns false if its odd.
def getNumber(st_index,end_index,array):
    if(array[end_index]==0):
        return True
    else:
        return False

getreader=raw_input().split(" ")
array=getInput(int(getreader[0]))
getQueries(int(getreader[1]),array)
