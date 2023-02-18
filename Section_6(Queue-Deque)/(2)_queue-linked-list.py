# Queue - Abstract Data Structure (ADT)
# Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). Queue follows First-In-First-Out methodology, i.e.,
# the data item stored first will be accessed first. A real-world example of queue can be a single-lane one-way road, where the vehicle enters first, exits first. More real-world examples can be seen as queues at the ticket windows and bus-stops.
#
# Representation of the queue:
#
# Dequeue  <-  [Data][Next][Data][Next][Data][Next][Data][Next]  <-  Enqueue
#
# Types of Queue
#
# There are four different types of queue that are listed as follows:
# Simple Queue or Linear Queue
# Circular Queue
# Priority Queue
# Double Ended Queue (or Deque)
#
# Queues in Python can be implemented either as Arrays or Linked List.
# This implementation uses Linked List.

# Node Class
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# LinkedListQueue Class

class LinkedListQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        newest = _Node(element, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return e

    def peek(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end=' <-- ')
            p = p._next
        print()

LinkedListQueue = LinkedListQueue()
LinkedListQueue.enqueue(5)
LinkedListQueue.enqueue(3)
LinkedListQueue.enqueue(8)
LinkedListQueue.display()
print('Length: ', len(LinkedListQueue))
LinkedListQueue.enqueue(7)
LinkedListQueue.enqueue(12)
LinkedListQueue.display()
print('Length: ', len(LinkedListQueue))
i = LinkedListQueue.dequeue()
print('Element removed: ', i)
LinkedListQueue.display()
print('Length: ', len(LinkedListQueue))
j = LinkedListQueue.peek()
print('Element at top: ', j)