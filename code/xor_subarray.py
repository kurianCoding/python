## this is a program which returns the XOR
## of all the sub arrays of a given array

row=raw_input().split(" ")
summation=0
for i in range(len(row)):
    summation=summation+int(row[i])
if summation%2==0:
    print 1 
else :
    print 0
