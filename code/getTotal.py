def getTotal(number):
    total=0
    q=1
    while(q>0):
        q=number/10
        total=total+number%10
        number=q

    total=total%10
    return total

inputnumber=int(raw_input())

if(inputnumber<0):
    print -1*getTotal(-1*inputnumber)
elif(inputnumber==0):
    print 0
else:
    print getTotal(inputnumber)
