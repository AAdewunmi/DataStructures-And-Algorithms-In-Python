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
