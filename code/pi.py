## this is a program which successively prints the value of pi 
## the longer you keep this on

from __future__ import division

## this function is the inverse sum
def isuma(a,b):
    return (b*a+1)/b

## this is the function for inverse diff
def idiff(a,b):
    if(a>b):
        return (b*a-1)/a
    else:
        return (a*b-1)/b

total=1

## this is the function which itrates the value for pi, even after
## a thousand iterations the value is far from being perfect
for i in range(1,1111):
    if(i%2==0):
        total=isuma(total,2*i+1)
    else:
        total=idiff(total,2*i+1)
    i=i+1
    print i-1,total*4
