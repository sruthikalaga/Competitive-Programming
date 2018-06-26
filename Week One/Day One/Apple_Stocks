def MaxProfit(list):
    a = len(list)
    if (a<2):
        raise Exception
    else:
        low = lis[0]
        diff = list[1]-list[0]
        for i in range(1,a):
            n = list[i]
            if(n-low > diff):
                diff = n-low
            if(n<low):
                low = n
        return diff
