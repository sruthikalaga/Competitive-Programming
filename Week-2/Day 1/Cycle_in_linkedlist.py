import unittest


def contains_cycle(f_node):
    copy1=f_node
    copy2=f_node
    while(copy1!=None and copy2!=None and copy2.next!=None ):
        copy1=copy1.next
        copy2=copy2.next.next
        if(copy1==copy2):
            return True

    return False
