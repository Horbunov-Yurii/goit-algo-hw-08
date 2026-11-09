class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Test cases
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)
print(find_min(root))