import unittest


def delete_node(delete_node):
    val_of_node = delete_node.next.value
    delete_node.next = delete_node.next.next
    delete_node.value = val_of_node
