import unittest


def is_valid(code):

    # Determine if the input code is valid
    validate = []
    for i in code:
        if(i=='(' or i=='[' or i=='{'):
            validate.append(i)
        else:
            if(len(validate)>0):
                check = validate.pop()
                if(ord(i)-ord(check)!=1 and ord(i)-ord(check)!=2 ):
                    return False
            else:
                return False

    if(len(validate)==0):
        return True
    else:
        False
