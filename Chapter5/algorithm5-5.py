"""
    전위 순회, 중위 순회, 후위순회
"""

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if (n is not None):
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if (n is not None):
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

def postorder(n):
    if (n is not None):
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")


d = TNode("D", None, None)
e = TNode("E", None, None)
b = TNode("B", d, e)
f = TNode("F", None, None)
c = TNode("C", f, None)
root = TNode("A", b, c)

# print("Pre-Order: ", preorder(root))
# print("In-Order: ", inorder(root))
# print("Post-Order: ", postorder(root))

print("Pre-Order: ", end=" ")
preorder(root)
print()

print("In-Order: ", end=" ")
inorder(root)
print()

print("Post-Order: ", end=" ")
postorder(root)
print()
