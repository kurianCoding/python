## this program is given an array, nth number in the array represents
## a power of 2 to the power n, i.e if nth is q then it represents (2**n)**q
## in order to minimise the sum of numbers of this array we are allowed
## to shift a lower power entry to a higher power entry. for example a power
## nth entry being 2q can be shifted to the n+1 th entry as q. in put will
## be a number which indicates the number of elements of the array followed
## by the array. output will be the sum which is minimum after reduction.

## the input to this function will be the array which is to be minimized
## output will be the minimized array with only those entries which are
## non zero.
def shiftRight(array):
    nextup=0
    res=[]
    for i in range (len(array)):
        if (array[i])%2==0:
            nextup=(array[i]+nextup)/2
            if (i==len(array)-1):
                res.append(nextup)
                res.append(0)
                return  shiftRight(res)
        else:
            res.append(array[i]+nextup)
            nextup=0

    return res
print shiftRight([1,2,1])
