#for binary search array has to be in 
#sorted accending
def binarySearch (arr,l,r,x):
    if r>=l:
        mid=l+(r-l)/2
        if arr[mid] == x:
            #if the indes is in the images
            return mid
        elif arr[mid] > x:
            #taking the upper array
            return binarySearch(arr,l,mid-1,x)
        else:
            #taking the lower array
            return binarySearch(arr,mid+1,r,x)
    else:
        #if x is not there in array
        return -1
arr=[0,1,2,3,6,7,9,72]
print binarySearch(arr,0,len(arr)-1,3)
