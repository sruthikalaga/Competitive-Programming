import unittest

def get_closing_paren(string, openning_index):

    countstring = 0
    l = len(string)
    for i in range (openning_index+1,l):
        if(string[i]=='('):
            countstring+=1;
        elif(string[i]==')'):
            if(countstring == 0):
                return i
            else:
                countstring-=1

    raise Exception
