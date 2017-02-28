## this program takes a subsequence, it accepts n
## queries from user and after each query returns the
## length of the the longest subsequence. this subsequence
## is not nessecarily contigous.

## this function takes in an array and finds the length of
## the greatest subsequence in that array
def subSq(array):
    count=0
    largest=0
    for i in range(len(array)):
        if array[i]>=largest:
        if array[i]<array[i+1]:
            count++
        else:
            largest=array[i]
            continue
