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
