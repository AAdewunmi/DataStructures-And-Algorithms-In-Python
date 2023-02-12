# Doubly Linked List
# ========================
# Definition: Double Linked List is a complex type of linked list in which a node
# contains a pointer to the previous as well as the next node in the sequence.
# Therefore, in a doubly linked list, a node consists of three parts: node data,
# pointer to the next node in sequence (next pointer), pointer to the previous node
# (previous pointer).
#
# Doubly Linked List Illustration
# HEAD -> [prev][data][next] -><- [prev][data][next] -><- [prev][data][next] -> NULL
# NULL <-
#
# (1.) Node Class
class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

# (2.) Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size == 0

    def is_empty(self):
        return self._size == 0

# (3.) Implement add_last()
# Implement add element to end of Doubly Linked List
    def add_last(self, element):
        newest = _Node(element, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

# (4.) Implement display()
# Implement display all the elements in a Double Linked List
    def display(self):
        p = self._head
        while p:
            print(p._element, end=' --> ')
            p = p._next
        print()