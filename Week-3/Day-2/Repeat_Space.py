import unittest

def find_repeat(arrList):

    upper = len(arrList)-1
    lower = 1
    while(lower<upper):
         middle = (lower+upper)//2
         lowlower = lower
         lowupper = middle
         uplower = middle+1
         upupper = upper
         ldist = lowupper - lowlower + 1
         count = 0
         for var1 in arrList:
             if(var1>=lowlower and var1<=lowupper):
                 count+=1
         if (count>ldist):
             lower = lowlower
             upper = lowupper
         else:
             lower = uplower
             upper = upupper
    return lower
