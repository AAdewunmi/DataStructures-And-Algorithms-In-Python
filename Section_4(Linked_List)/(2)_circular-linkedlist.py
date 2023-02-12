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
#
# Circular Linked List Illustration
# HEAD -> [data][next] -> [data][next] -> [data][next] ->
#   <-             <-             <-              <-
#

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

# (2). Implement addlast()
# Implement add element to end of Circular Linked List
    def add_last(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

# (3). Implement display()
# Implement display all elements in a Circular Linked List
    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end= ' --> ')
            p = p._next
            i = i + 1
        print()

# (4). Implement addfirst()
# Implement insert an element at the start of a Circular Linked List
    def add_first(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            newest._next = newest
            self._head = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

# (5). Implement addany()
# Implement add element anywhere inbetween the Circular Linked List
    def add_any(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next = newest
        self._size += 1

# (6). Implement remove_first()
# Implement delete an element at the beginning of a Circular Linked List
    def remove_first(self):
        if self.is_empty():
            print('Circular List is Empty')
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._head = None
            self._tail = None
        return e

# (7). Implement remove_last()
# Implement delete at end of Circular Linked List
    def remove_last(self):
        if self.is_empty():
            print('Circular List is Empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._tail = p
        p = p._next
        self._tail._next = self._head
        e = p._element
        self._size -= 1
        return e

# (8). Implement remove_any()
# Implement delete element anywhere in between Circular Linked List
    def remove_any(self, position):
        p = self._head
        i = 1
        while i < position -1:
            p = p._next
            i = i + 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e

CircularLinkedList = CircularLinkedList()
CircularLinkedList.add_last(3)
CircularLinkedList.add_last(5)
CircularLinkedList.add_last(2)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
CircularLinkedList.add_first(9)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
CircularLinkedList.add_any(20, 3)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
j = CircularLinkedList.remove_first()
print('Element Removed: ', j)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
k = CircularLinkedList.remove_last()
print('Element Removed: ', k)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
CircularLinkedList.add_last(33)
CircularLinkedList.add_last(55)
CircularLinkedList.add_last(22)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)
l = CircularLinkedList.remove_any(2)
print('Element Removed: ', l)
CircularLinkedList.display()
i = CircularLinkedList.__len__()
print('Size: ', i)