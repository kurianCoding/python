## this program will take an array of numbers
## it will then answer n queries where each query
## will ask the same question, what is the index(s) of 
## this number in the array. if the number does not exist
## the answer should be 'E'

## this function takes in an array, an upper limit and a
## lower limit and a number. It returns the new upper and
## lower limits for the array.
def binarySearch(array,upper_limit,lower_limit,number):
    print array,upper_limit,lower_limit
    if(array[upper_limit]>number):
        if(array[lower_limit]<number):
                if(array[(lower_limit+upper_limit)/2]==number):
                    return 1+ (lower_limit+upper_limit)/2
                elif(array[(lower_limit+upper_limit)/2]>number):
                    return binarySearch(array,(upper_limit+lower_limit)/2-1,lower_limit,number)
                else:
                    return binarySearch(array,upper_limit,(upper_limit+lower_limit)/2+1,number)
        elif(array[lower_limit]==number):
            return lower_limit+1
        elif(array[upper_limit]==number):
            return upper_limit+1
    elif(array[upper_limit]==number):
        return upper_limit+1
    else:
        return False
## this function takes in an array and a number and calls
## the binarySearch function. if it recives a number it prints
## the number if it recieves false it will just print 'E'
def wrapBinary(array,searchTerm):
    result=binarySearch(array,0,len(array)-1,searchTerm)
    if(result==False):
        print 'E'
    else:
        print result
    return

wrapBinary([1,2,4,6,10,11,25],1)
wrapBinary([1,2,4,6,10,11,25],25)
wrapBinary([1,2,4,6,10,11,25],10)
wrapBinary([1,2,4,6,10,11,25],6)
