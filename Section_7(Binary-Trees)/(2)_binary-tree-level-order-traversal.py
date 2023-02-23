from queuelinkedlist import LinkedListQueue
class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, element, left, right):
        self._root = _Node(element, left._root, right._root)

    # Preorder: RoLR
    # Inorder: LRoR
    # Postorder:LRRo
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

    def levelorder(self):
       Q = LinkedListQueue()
       t = self._root
       print(t._element, end='-->')
       Q.enqueue(t)
       while not Q.is_empty():
           t = Q.dequeue()
           if t._left:
               print(t._left._element, end='-->')
               Q.enqueue(t._left)
           if t._right:
               print(t._right._element, end='-->')
               Q.enqueue(t._right)
    def count(self, root):
       if root:
           x = self.count(root._left)
           y = self.count(root._right)
           return x + y + 1
       return 0

    def height(self, root):
        if root:
            x = self.height(root._left)
            y = self.height(root._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

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
print('\nLevel order Traversal')
c.levelorder()
print('\nNumber of Nodes')
print(c.count(c._root))
print('Height of Tree')
print(c.height(c._root))