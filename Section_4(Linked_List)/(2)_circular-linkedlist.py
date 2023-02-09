# Circular Linked List
# ========================
# Definition:
# A circular linked list is a variation of a singly linked list.
# The only difference between the singly linked list and a circular linked list
# is that the last node does not point to any node in a singly linked list, so
# its link part contains a NULL value.
# On the other hand, the circular linked list is a list in which the last node
# connects to the first node, so the link part of the last node holds the first
# node's address. The circular linked list has no starting and ending node.
# We can traverse in any direction, i.e., either backward or forward.


# (1). Creating and displaying a Circular Linked List
# Node Class
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# Circular Linked List Class
class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0