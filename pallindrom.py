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

    :arg1: TODO
    :returns: TODO

    """
    pass
def splitMiddle(arg1):
    """TODO: Docstring for function.to split any given string to two equal halves

    :arg1: string to be split 
    :returns: two parts 

    """

def checkPallindrome(arg1):
    """a funciotn to check if a string is a pallindrome

    :arg1: is the string to be checked 
    :returns: a string  

    """
    string=arg1
    first,second=splitMiddle(string)
    if(stringCompare(first,reverseString(second)):
            return "is Palindrome"
    else:
            return"not Palindrome"

 string = raw_input() 
 print checkPallindrome(string)
