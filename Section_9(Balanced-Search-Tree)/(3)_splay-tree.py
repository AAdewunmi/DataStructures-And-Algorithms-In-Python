# Splay Tree
# ==========
# A Splay tree is a self-adjusting binary search tree invented by Sleator and Tarjan. Unlike an AVL tree (or a Red-Black tree), the structure of the splay tree changes even after the search operation.
# Every time we search an item x or insert x, it moves x to the root of the tree so that the next access of x is quick.
# The goal of the splay tree is not to make every operation fast rather make the sequence of operations fast.
# The individual operation in the splay tree can, sometimes, take O(n) time making the worst case running time linear.
# The sequence of operations, however, take O(logn) amortized time per operation. In other words, the sequence of M operations takes O(Mlogn) time.
# Since the splay tree adjusts itself according to usage, it performs much more efficiently than other binary search trees if the usage pattern is skewed.
# Unlike an AVL or a Red-Black tree where the tree must maintain their invariants all the time, the structure of the splay tree can be in any arbitrary state (although it should maintain the binary search tree invariants all the time)
# but during every operation, it restructures the tree to improve the efficiency of future (incoming) operations.
# The splay tree moves a node x to the root of the tree by performing series of single and double tree rotations.
# Each double rotations moves x to its grandparent’s place and every single rotation moves x to its parent’s place.
# We perform these rotations until x reaches to the root of the tree. This process is called splaying.
# Besides moving x to the root, splaying also shortens the height of the tree which makes the tree more balanced.
#
# There are two types of single rotations and four types of double rotations. Each of them is explained in detail below.
#
# Zig Rotation: Zig is a single rotation. We do zig rotation on node x if x is a left child and x does not have a grandparent (i.e. x’s parent is a root node).
# To make the zig rotation, we rotate x’s parent to the right.
#
# Zag Rotation: Zag rotation is a mirror of zig rotation. We do zag rotation on node x if x is a right child and x does not have a grandparent.
# To make the zag rotation, we perform a left rotation at x’s parent node.
#
# Zig-Zig Rotation: Zig-Zig is a double rotation. We do a zig-zig rotation on x when x is a left child and x’s parent node is also a left child.
# The zig-zig rotation is done by rotating x’s grandparent node to the right followed by right rotation at x’s parent node.
#
# Zag-Zag Rotation: Zag-Zag rotation is a mirror of zig-zig rotation. We do zag-zag rotation on x if x is a right child and x’s parent is also a right child.
# To make the zag-zag rotation, we first do a left rotation at x’s grandparent and then do the left rotation at x’s parent node.
#
# Zig-Zag Rotation: Zig-zag rotation is also a double rotation. We perform zig-zag rotation on x when x is a right child and x’s parent is a left child.
# Zig-zag rotation is done by doing a left rotation at x’s parent node followed by right rotating x grandparent (new parent) node.
#
# Zag-Zig Rotation: The last rotation is the zag-zig rotation. It is a mirror of zig-zag rotation.
# To do zag-zig rotation on node x, we do the right rotation at x’s parent node and left rotation at x grandparent (new parent) node.
#
# Text Source:
# Title: Splay Trees (with implementations in C++, Java, and Python)
# Author: Algorithm Tutor
# URL: https://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/
#
# Splay tree implementation in Python
# Author: AlgorithmTutor
# Tutorial URL: http://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def __print_helper(self, currPtr, indent, last):
        # print the tree structure on the screen
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.data)

            self.__print_helper(currPtr.left, indent, False)
            self.__print_helper(currPtr.right, indent, True)

    def __search_tree_helper(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def __delete_node_helper(self, node, key):
        x = None
        t = None
        s = None
        while node != None:
            if node.data == key:
                x = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if x == None:
            print
            "Couldn't find key in the tree"
            return

        # split operation
        self.__splay(x)
        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

        # join operation
        if s.left != None:
            s.left.parent = None

        self.root = self.__join(s.left, t)
        s = None

    # rotate left at node x
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # Splaying operation. It moves x to the root of the tree
    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.__right_rotate(x.parent)
                else:
                    # zag rotation
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    # joins two trees s and t
    def __join(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.maximum(s)
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

    def __pre_order_helper(self, node):
        if node != None:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.std.out.write(node.data + " ")

    # Pre-Order traversal
    # Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__pre_order_helper(self.root)

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        self.__in_order_helper(self.root)

    # Post-Order traversal
    # Left Subtree -> Right Subtree -> Node
    def postorder(self):
        self.__post_order_helper(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def search_tree(self, k):
        x = self.__search_tree_helper(self.root, k)
        if x != None:
            self.__splay(x)

    # find the node with the minimum key
    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not null,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not null,
        # the predecessor is the rightmost node in the
        # left subtree
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y


