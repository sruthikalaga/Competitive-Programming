def findfloor(input):   
    inc = 13
    cur = 14
    llimit = 1
    iter = 1
    while(cur!=input):
        print('current',cur)
        if (cur>input):
            cur = llimit
            print('iteration -',iter)
            while(cur!=input):      
                print ('current',cur)
                print ('iteration -',iter)
                cur+=1
                iter+=1
        elif (cur<input):
            print ('iteration -',iter)
            iter+=1
            llimit+=inc+1
            cur+=inc        
            inc-=1
    print('found the floor in',iter,'iteration')
