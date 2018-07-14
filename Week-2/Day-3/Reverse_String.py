import unittest

def reverse(list_of_chars):
    lenoflist = len(list_of_chars)
    if(lenoflist == 0 or lenoflist == 1):
        return list_of_chars 
    halflist = (lenoflist//2)
    for i in range (halflist):
        (list_of_chars[i], list_of_chars[lenoflist-i-1] ) = (list_of_chars[lenoflist-i-1], list_of_chars[i])
    return list_of_chars
