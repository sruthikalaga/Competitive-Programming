import unittest


def kth_to_last_node(kth, head):

    if kth == 0:
        raise Exception
    firstnode = head
    lastnode = head
    for i in range (kth):
        lastnode = lastnode.next
    while(lastnode!=None):
        firstnode = firstnode.next
        lastnode = lastnode.next
    
    return firstnode
