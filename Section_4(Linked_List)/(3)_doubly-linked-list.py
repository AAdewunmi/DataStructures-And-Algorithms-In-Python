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
        return self._size

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
# Implement display all the elements in a Doubly Linked List
    def display(self):
        p = self._head
        while p:
            print(p._element, end=' --> ')
            p = p._next
        print()

# (5.) Implement display_rev()
# Implement display all the elements in a Doubly Linked List in reverse order
    def display_rev(self):
        p = self._tail
        while p:
            print(p._element, end=' --> ')
            p = p._prev
        print


# (6.) Implement add_first()
# Implement insert element at the beginning of a Doubly Linked List
    def add_first(self, element):
        newest = _Node(element, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1

# (7.) Implement add_any()
# Implement insert an element anywhere in a Doubly Linked List
    def add_any(self, element, position):
        newest = _Node(element, None, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1

# (8.) remove_first()
# Implement delete an element at the beginning of a Doubly Linked List
    def remove_first(self):
        if self.is_empty():
            print('List is Empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

DoublyLinkedList = DoublyLinkedList()
DoublyLinkedList.add_last(2)
DoublyLinkedList.add_last(8)
DoublyLinkedList.add_last(5)
i = DoublyLinkedList.__len__()
print('Size:', i)
DoublyLinkedList.display()
DoublyLinkedList.display_rev()
print()
DoublyLinkedList.add_first(3)
i = DoublyLinkedList.__len__()
print('Size:', i)
DoublyLinkedList.display()
DoublyLinkedList.add_first(7)
i = DoublyLinkedList.__len__()
print('Size:', i)
DoublyLinkedList.display()
DoublyLinkedList.add_any(55, 3)
i = DoublyLinkedList.__len__()
print('Size:', i)
DoublyLinkedList.display()
j = DoublyLinkedList.remove_first()
print('Element: ', j)
i = DoublyLinkedList.__len__()
print('Size:', i)
DoublyLinkedList.display()