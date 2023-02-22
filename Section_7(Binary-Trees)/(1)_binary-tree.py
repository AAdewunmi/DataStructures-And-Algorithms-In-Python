# Binary Tree - Abstract Data Type
# ================================
# A Binary tree is made up of nodes, where each node contains a "left" pointer,
# a "right" pointer, and a data element.The "root" pointer points to the top most
# node in the tree. The left and right pointers recursively point to smaller "subtrees"
# on either side. A null pointer represents a binary tree with no elements -- the empty tree.
# The formal recursive definition is: a binary tree is either empty (represented by a null pointer),
# or is made up of a single node, where the left and right pointers (recursive definition ahead),
# each point to a binary tree.
#
# Binary Tree Illustration:
#
#                [Root Node] <- Parent
#                 /        \
#          [Left Node] [Right Node]  <- Siblings

# Implement Node Class
class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right

# Implement BinaryTree Class
class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, element, left, right):
        self._root = _Node(element, left._root, right._root)

    def preorder(self, root):
        if root:
            print(root._element, end='-->')
            self.preorder(root._left)
            self.preorder(root._right)

    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end='-->')
            self.inorder(root._right)

    def postorder(self, root):
        if root:
            self.postorder(root._left)
            self.postorder(root._right)
            print(root._element, end='-->')

# Example 1
print('Example 1')
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.maketree(20, a, a)
y.maketree(30, a, a)
z.maketree(10, x, y)
print('Preorder Traversal')
z.preorder(z._root)
print('\nInorder Traversal')
z.inorder(z._root)
print('\nPostorder Traversal')
z.postorder(z._root)

# Example 2
print('\nExample 2')
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
b = BinaryTree()
c = BinaryTree()
e = BinaryTree()
x.maketree(40, e, e)
y.maketree(20, x, e)
z.maketree(60, e, e)
a.maketree(50, e, z)
b.maketree(30, a, e)
c.maketree(10, y, b)
print('Preorder Traversal')
c.preorder(c._root)
print('\nInorder Traversal')
c.inorder(c._root)
print('\nPostorder Traversal')
c.postorder(c._root)