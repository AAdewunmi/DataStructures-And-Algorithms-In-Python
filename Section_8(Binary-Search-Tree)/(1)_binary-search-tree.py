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

class BinarySearchTree:

    def __init__(self):
        self._root = None

    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end='-->')
            self.inorder(root._right)

    # Iterative Insert function
    def insert_it(self, root, element):
        temp = None
        while root:
            temp = root
            if element == root._element:
                return
            elif element < root._element:
                root = root._left
            elif element > root._element:
                root = root._right
        n = _Node(element)
        if self._root:
            if element < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    # Recursive Insert function
    def insert_recur(self, root, e):
        if root:
            if e < root._element:
                root._left = self.insert_recur(root._left, e)
            elif e > root._element:
                root._right = self.insert_recur(root._right, e)
        else:
            n = _Node(e)
            root = n
        return root

    # Iterative Search function
    def search_it(self, key):
        root = self._root
        while root:
            if key == root._element:
                return True
            elif key < root._element:
                root = root._left
            elif key > root._element:
                root = root._right
        return False

    # Recursive Search function
    def search_recur(self, root, key):
        if root:
            if key == root._element:
                return True
            elif key < root._element:
                return self.search_recur(root._left, key)
            elif key > root._element:
                return self.search_recur(root._right, key)

    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c

BinarySearchTree = BinarySearchTree()
BinarySearchTree.insert_it(BinarySearchTree._root, 50)
BinarySearchTree.insert_it(BinarySearchTree._root, 30)
BinarySearchTree.insert_it(BinarySearchTree._root, 80)
BinarySearchTree.insert_it(BinarySearchTree._root, 10)
BinarySearchTree.insert_it(BinarySearchTree._root, 40)
BinarySearchTree.insert_it(BinarySearchTree._root, 60)
BinarySearchTree.inorder(BinarySearchTree._root)
print()
BinarySearchTree._root = BinarySearchTree.insert_recur(BinarySearchTree._root, 50)
BinarySearchTree.insert_recur(BinarySearchTree._root, 30)
BinarySearchTree.insert_recur(BinarySearchTree._root, 80)
BinarySearchTree.insert_recur(BinarySearchTree._root, 10)
BinarySearchTree.insert_recur(BinarySearchTree._root, 40)
BinarySearchTree.insert_recur(BinarySearchTree._root, 60)
BinarySearchTree.inorder(BinarySearchTree._root)
print()
print(BinarySearchTree.search_it(10))
print(BinarySearchTree.search_recur(BinarySearchTree._root, 10))
BinarySearchTree.delete(60)
BinarySearchTree.inorder(BinarySearchTree._root)