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
