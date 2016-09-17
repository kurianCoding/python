@classmethod
def stringCompare(arg1):
    """TODO: Docstring for stringCompare.finding if one string is equal to other

    :arg1: TODO

    :arg1: TODO
    :returns: TODO

    """
    pass
def reverseString(arg1):
    """TODO: Docstring for function. to reverse a given string.

    :arg1: a string 
    :returns: return the reversed string 

    """
    string=  arg1[::-1] 
    return string
def splitMiddle(arg1):
    """TODO: Docstring for function.to split any given string to two equal halves

    :arg1: string to be split 
    :returns: two parts 

    """
    length=len(arg1)
    part1=length/2

    if length%2==1:
        length_part1=part1
        length_part2=part1+1
    else:
        length_part1=part1
        length_part2=part1

    strpart1=arg1[:length_part1]
    strpart2=arg1[length_part2:length]
    return strpart1,strpart2

def checkPallindrome(arg1):
    """a funciotn to check if a string is a pallindrome

    :arg1: is the string to be checked 
    :returns: a string  

    """
    string=arg1
    first,second=splitMiddle(string)
    if stringCompare(first,reverseString(second)):
            return "is Palindrome"
    else:
            return"not Palindrome"

string = raw_input() 
 print checkPallindrome(string)
