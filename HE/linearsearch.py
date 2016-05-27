number=int(raw_input())
array=raw_input().split(" ")
for i in range(number):
    if (int(array[i])==5):
        print i
        break
if(i<number-1):
    print -1
