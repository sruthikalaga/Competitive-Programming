import unittest

def has_palindrome_permutation(input):
    lenstr = len(input)
    di = {}
    for i in range (lenstr):
        no = di.setdefault(input[i], 0)
        di[input[i]]=no+1
        
    if (lenstr%2==0):
        for var in di.keys():
            if (di[var]%2!=0):
                return False
    else:
        f = False
        for var in di.keys():
            if (di[var]%2!=0):
                if(f == True):
                    return False
                else:
                    f = True
    return True
