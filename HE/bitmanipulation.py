testcases=int(raw_input())
for i in range(testcases):
    test=int(raw_input())
    count=1
    quotient=test
    while(quotient>2):
        quotient=test/2
        remainder=test%2
        count=count+remainder
        test=quotient
    print count
