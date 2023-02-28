# AVL Tree
#
# AVL tree is a self-balancing binary search tree in which each node maintains extra information called a balance factor
# whose value is either -1, 0 or +1. AVL tree got its name after its inventor Georgy Adelson-Velsky and Landis.
#
# Balance Factor:
# Balance factor of a node in an AVL tree is the difference between the height of the left subtree and that of the right subtree of that node.
# Balance Factor = (Height of Left Subtree - Height of Right Subtree) or (Height of Right Subtree - Height of Left Subtree)
# The self-balancing property of an avl tree is maintained by the balance factor. The value of balance factor should always be -1, 0 or +1.
#
# Operations of an AVL tree:
# Left Rotate: In left-rotation, the arrangement of the nodes on the right is transformed into the arrangements on the left node.
# Right Rotate: In left-rotation, the arrangement of the nodes on the left is transformed into the arrangements on the right node.
# Left-Right Rotate: In left-right rotation, the arrangements are first shifted to the left and then to the right.
# Right-Left Rotate: In right-left rotation, the arrangements are first shifted to the right and then to the left.
#
# AVL Tree implementation in Python
# Source:
# AVL Tree
# Programiz.com
# URL: https://www.programiz.com/dsa/avl-tree

import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

