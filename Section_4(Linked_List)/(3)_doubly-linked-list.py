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