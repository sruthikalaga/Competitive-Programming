import unittest

def is_single_riffle(half1, half2, shuffled_deck):

    len_deck = len (shuffled_deck)
    len1 = len(half1)
    len2 = len(half2)
    var1 = 0
    var2 = 0
    for var3 in range (len_deck):
        if(var1<len1 and shuffled_deck[var3] == half1[var1]):
            var1+=1
        elif(var2<len2 and shuffled_deck[var3] == half2[var2]):
            var2+=1
        else:
            return False
    return True
