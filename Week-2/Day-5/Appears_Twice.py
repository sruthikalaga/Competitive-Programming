import unittest

def find_repeat(listnum):

    # Find the number that appears twice
    n = len(listnum)
    for i in range (n):
        print('-----'+str(i))
        if(listnum[abs(listnum[i])] > 0) :
            listnum[abs(listnum[i])] = (-1) * listnum[abs(listnum[i])]
            print(listnum[abs(listnum[i])])
        else :
            return abs(listnum[i])
