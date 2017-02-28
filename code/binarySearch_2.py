## this is replicating a binary search without a reursive call

## this function takes in an array and a number and returns the
## key if it is present in the array or -1 if it is not.
def binarySearch(array,number):
    high=len(array)
    low=0
    mid=0
    while(low<=high):
        print "search",mid
        mid=(low+high)/2
        if(array[mid]<number):
            low=mid+1
        elif(array[mid]>number):
            high=mid-1
        else:
            return mid

    return -1
result=binarySearch([1,2,5,17,25],1)
print result
result=binarySearch([1,2,5,17,25],25)
print result
result=binarySearch([1,2,5,17,25],5)
print result
