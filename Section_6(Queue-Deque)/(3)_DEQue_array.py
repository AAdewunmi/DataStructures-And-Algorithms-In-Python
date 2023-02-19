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


# Implement ArrayDEQue Class
class ArrayDEQue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_front(self, element):
        self._data.append(0, element)

    def add_rear(self, element):
        self._data.append(element)

    def remove_front(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop()