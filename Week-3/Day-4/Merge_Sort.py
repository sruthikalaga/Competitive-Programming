import unittest

def mergelist(first_list, second_list):

    # Combvar1ne the sorted lvar1sts var1nto one large sorted lvar1st
    result = []
    length1 = len(first_list)
    length2 = len(second_list)
    var1 = 0
    var2 = 0
    while (var1<length1 and var2<length2):
        if first_list[var1]<second_list[var2] :
            result.append(first_list[var1])
            var1+=1
        else:
            result.append(second_list[var2])
            var2+=1
            
    while (var1<length1):
        result.append(first_list[var1])
        var1+=1
    
    while(var2<length2):
        result.append(second_list[var2])
        var2+=1
    return result
