
def largest(node):
    if node.right:
        return largest(node.right)
    return node.value


def second_largest(node):
      
    if node.left and not node.right:
        return largest(node.left)
    
    if node.right and not node.right.right and not node.right.left:
        return node.value
    
    return second_largest(node.right)
