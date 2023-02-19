# DEQue (or Double Ended Queue) - Abstract Data Structure (ADT)
# =============================================================
#
# Definition: In DEQue or Double Ended Queue, insertion and deletion can be done from both ends of the
# queue either from the front or rear. It means that we can insert and delete from front and rear ends of the
# queue. Deque can be used as a palindrome checker meaning that if we read the string from both ends,
# then the string would be the same.
# Deque can be used both as stack and queue as it allows the insertion and deletion operations on both ends.
# Deque can be considered as a stack because stack follows the LIFO (Last In First Out) principle in which
# insertion and deletion both can be performed only from one end. And in DEQue, it is possible to perform
# both insertion and deletion from one end, and DEQue does not follow the FIFO principle.
#
# Representation of the DEQue:
#
#             Front                   Rear
# INSERT ->  [Data][Data][Data][Data][Data] <- INSERT
# DELETE <-                                 -> DELETE

# Implementation of DEQue using Linked List Data Structure
#
# LinkedListDEQue Class
# Node Class
# ==========
class _Node(object):
    __slots__ = '_element', '_next'

    # Constructor
    def __init__(self, element, next):
        self._element = element
        self._next = next


# Linked List Class
# ===========
class LinkedList:
    # Constructor
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Find length of the Linked List
    def __len__(self):
        return self._size

    # Check whether Linked List is empty
    def is_empty(self):
        return self._size == 0

    # Add Nodes to the back of the Linked List
    def add_last(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    # Traverse the Linked List and display elements
    def display(self):
        p = self._head
        while p:
            print(p._element, end=' --> ')
            p = p._next
        print()

    # Search for an element in a Linked List
    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    # Add Nodes to the front of the Linked List
    def add_first(self, key):
        newest = _Node(key, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    # Add Nodes to any position in a Linked List
    def add_any(self, key, position):
        newest = _Node(key, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    # Remove an element from the beginning of a Linked List
    def remove_first(self):
        if self.is_empty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    # Remove an element from the end of a Linked List
    def remove_last(self):
        if self.is_empty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        return e

    # Remove an element at any position in a Linked List
    def remove_any(self, position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e

LinkedList = LinkedList()
LinkedList.add_last(7)
LinkedList.add_last(4)
LinkedList.display()
print(LinkedList.__len__())
i = LinkedList.search(7)
print('Index: ', i)
LinkedList.add_first(15)
LinkedList.display()
print(LinkedList.__len__())
LinkedList.add_first(23)
LinkedList.display()
print(LinkedList.__len__())
LinkedList.add_any(20, 3)
LinkedList.display()
print(LinkedList.__len__())
LinkedList.add_any(100, 5)
LinkedList.display()
print(LinkedList.__len__())
i = LinkedList.remove_first()
print('Element removed: ', i)
LinkedList.display()
print(LinkedList.__len__())
i = LinkedList.remove_last()
print('Element removed: ', i)
LinkedList.display()
print(LinkedList.__len__())
LinkedList.remove_any(3)
print('Element removed: ', i)
LinkedList.display()
print(LinkedList.__len__())
i = LinkedList.remove_any(2)
print('Element removed: ', i)
LinkedList.display()
print(LinkedList.__len__())