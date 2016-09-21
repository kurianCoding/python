test=int(raw_input())
for i in range(test):
    number=raw_input()
    if("21" in number):
        print "the streak is broken!"
        continue
    if(int(number)%21==0):
        print "the streak is broken!"
        continue
    print "The streak lives still in our heart!"

