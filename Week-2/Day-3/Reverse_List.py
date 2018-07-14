import unittest


def reverse(head):
    if(head == None or head.next == None):
        return head
    
    previous = head
    current = head.next
    save = None
    head.next = None
    while(current.next!=None):
        save = current.next
        current.next = previous
        previous = current
        current = save
        
    current.next = previous
    return current
