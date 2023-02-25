# Binary Search Tree
# ==================
# Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
#
#     It is called a binary tree because each tree node has a maximum of two children.
#     It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.
#
# The properties that separate a binary search tree from a regular binary tree is
#
#     All nodes of left subtree are less than the root node
#     All nodes of right subtree are more than the root node
#     Both subtrees of each node are also BSTs i.e. they have the above two properties

# Implement Node Class
class _Node:

    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

# Implement Binary Search Tree using Linked representation. It is similar in structure to
# a Linked list but not a Linked List.

