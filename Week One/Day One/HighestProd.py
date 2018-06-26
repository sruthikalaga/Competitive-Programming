
def HighestProd(list1):
    
    l = len(list1)
    if l<3:
        raise Exception("Exception Raised")
    l1 = sorted(list1)

    p = l1[l - 1] * l1[l - 2] * l1[l - 3]
    q = l1[l - 1] * l1[0] * l1[1]

    if p > q:
        return p
    else:
        return q
