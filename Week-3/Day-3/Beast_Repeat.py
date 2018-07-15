import unittest

def find_duplicate(list):

    lenlist = len(list)
    list1 = lenlist
    list2 = lenlist
    while True:
        list1 = list[list1-1]
        list2 = list[list[list2-1]]
        if list1 == list2:
            break

    list2 = lenlist
    while True:
        list1 = list[list1-1]
        list2 = list[list2-1]
        if list2 == list1:
            return list1
