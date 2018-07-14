import unittest

def get_permutations(input):
    ans = []
    leninput = len(input)
    if(leninput==0 or leninput==1):
        return set([input])
    for var in range (leninput):
        new = input[0:var]+input[var+1:leninput]
        lis = get_permutations(new)
        for k in lis:
            ans.append(input[var]+k)
    return set(ans)
