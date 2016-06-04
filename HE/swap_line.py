def swap(arg):
    line_len=len(arg)
    for i in range(line_len):
        if(arg[i]==arg[i-1]):
            print i,arg[i]

            

test_cases=int(raw_input())
for i in range(test_cases):
    pupil_count=2*int(raw_input())
    line=raw_input()
    swap(line) 
