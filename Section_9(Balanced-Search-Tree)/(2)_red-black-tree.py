# Red-Black Tree
# ==============
# Red-Black tree is a self-balancing binary search tree in which each node contains
# an extra bit for denoting the color of the node, either red or black.
#
# A red-black tree satisfies the following properties:
# 1. Red/Black Property: Every node is colored, either red or black.
# 2. Root Property: The root is black.
# 3. Leaf Property: Every leaf (NIL) is black.
# 4. Red Property: If a red node has children then, the children are always black.
# 5. Depth Property: For each node, any simple path from this node to any of its
# descendant leaf has the same black-depth (the number of black nodes).
#
# Each node has the following attributes:
#     color
#     key
#     leftChild
#     rightChild
#     parent (except root node)
#
# How the red-black tree maintains the property of self-balancing?
# The red-black color is meant for balancing the tree.
# The limitations put on the node colors ensure that any simple path from the root
# to a leaf is not more than twice as long as any other such path. It helps in maintaining
# the self-balancing property of the red-black tree.
#
# Operations on a Red-Black Tree
# Left Rotate: In left-rotation, the arrangement of the nodes on the right is transformed into the arrangements on the left node.
# Right Rotate: In right-rotation, the arrangement of the nodes on the left is transformed into the arrangements on the right node.
# Left-Right Rotate: In left-right rotation, the arrangements are first shifted to the left and then to the right.
# Right-Left Rotate: In right-left rotation, the arrangements are first shifted to the right and then to the left.
#
#
# Implementing Red-Black Tree in Python
# Source:
# AVL Tree
# Programiz.com
# URL: https://www.programiz.com/dsa/red-black-tree

import sys

# Node creation
class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Preorder
    def pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)