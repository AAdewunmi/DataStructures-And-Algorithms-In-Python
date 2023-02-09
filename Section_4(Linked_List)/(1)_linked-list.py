# Linked List
# ========================
# Definition:
# Linked list is a linear data structure that includes a series of connected nodes.
# Linked list can be defined as the nodes that are randomly stored in the memory.
# A node in the linked list contains two parts, i.e., first is the data part and second is the address part.
# The last node of the list contains a pointer to the null. After array, linked list is the second most used data structure.
# In a linked list, every link contains a connection to another link.


# (1). Why do we use Linked List?
#
# Linked list is a data structure that overcomes the limitation of arrays.
# These include:
# - The size of the array must be known in advance.
# - Increasing the size of the array is a time-consuming task.
# - All the elements in the array need to be contiguously stored in the memory.
#   Inserting an element in the array needs shifting of all its predecessors.
#
# Linked list is useful because:
# - It dynamically allocates memory. All the nodes of the linked list are non-contiguously
#   stored in memory and linked together with the help of pointers.
# - In a linked list, size is no longer a problem since we do not have to define its size at the time of declaration.
#   A List grows as per the program's demand and limited to the available memory space.


# (2). Implement Node Class
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

              #Head                                #Tail
# Linked List [7][] -> [4][] -> [12][] -> [8][] -> [3][Null]

n1 = _Node(7, None)  # n1._element = 7, n1._next = None (Link to n2)
n2 = _Node(4, None)  # n2._element = 4, n2._next = None


# (3). Implement a Linked List
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

# (4). Implement search()
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

# (5). Implement addfirst()
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

# (6). Implement addany()
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

# (7). Implement removefirst()
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

# (8). Implement removelast()
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

#==========
# Test Linked List Class
#==========


LinkedList = LinkedList()
LinkedList.add_last(7)
LinkedList.add_last(4)
LinkedList.display()
print('Size :', LinkedList.__len__())
i = LinkedList.search(7)
print('Index: ', i)
LinkedList.add_first(15)
LinkedList.display()
print('Size :', LinkedList.__len__())
LinkedList.add_first(23)
LinkedList.display()
print('Size :', LinkedList.__len__())
LinkedList.add_any(20, 3)
LinkedList.display()
print('Size :', LinkedList.__len__())
LinkedList.add_any(100, 5)
LinkedList.display()
print('Size :', LinkedList.__len__())
i = LinkedList.remove_first()
print('Element removed: ', i)
LinkedList.display()
print('Size :', LinkedList.__len__())
i = LinkedList.remove_last()
print('Element removed: ', i)
LinkedList.display()
print('Size :', LinkedList.__len__())

