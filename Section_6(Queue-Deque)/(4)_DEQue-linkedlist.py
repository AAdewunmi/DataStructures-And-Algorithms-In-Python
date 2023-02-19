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


# LinkedListDEQue Class
# ===========
class LinkedListDEQue:
    # Constructor
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    # Find length of the DEQue
    def __len__(self):
        return self._size

    # Check whether DEQue is empty
    def is_empty(self):
        return self._size == 0

        # Add Nodes to the back of the DEQue
    def add_last(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    # Add Nodes to the front of the DEQue
    def add_first(self, key):
        newest = _Node(key, None)
        if self.is_empty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1

    # Remove an element from the beginning of a DEQue
    def remove_first(self):
        if self.is_empty():
            print('List is empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return e

    # Remove an element from the end of a DEQue
    def remove_last(self):
        if self.is_empty():
            print('List is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1
        return e


    # Traverse the DEQue and display elements
    def display(self):
        p = self._front
        while p:
            print(p._element, end=' --> ')
            p = p._next
        print()

    # Gets the element at the front of the DEQue without removing it.
    def peek(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._front._element

    # Gets the element at the back of the DEQue without removing it.
    def rear(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._rear._element

LinkedListDEQue = LinkedListDEQue()
LinkedListDEQue.add_first(5)
LinkedListDEQue.add_first(3)
LinkedListDEQue.add_first(7)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
LinkedListDEQue.add_last(2)
LinkedListDEQue.add_last(8)
LinkedListDEQue.add_last(6)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
i = LinkedListDEQue.remove_first()
print('Remove first element: ', i)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
j = LinkedListDEQue.remove_last()
print('Remove last element: ', j)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
k = LinkedListDEQue.peek()
print('Front element: ', k)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
l = LinkedListDEQue.rear()
print('Back Element: ', l)
LinkedListDEQue.display()
print('Length: ', len(LinkedListDEQue))
