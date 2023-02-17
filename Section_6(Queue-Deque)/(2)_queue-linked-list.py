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