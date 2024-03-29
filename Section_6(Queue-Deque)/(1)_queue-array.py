# Queue - Abstract Data Structure (ADT)
# =====================================
# Definition: Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). Queue follows First-In-First-Out methodology, i.e.,
# the data item stored first will be accessed first. A real-world example of queue can be a single-lane one-way road, where the vehicle enters first, exits first. More real-world examples can be seen as queues at the ticket windows and bus-stops.
#
# Representation of the queue:
#
# Dequeue  <- [Data][Data][Data][Data]  <- Enqueue
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
# This implementation uses Arrays.

# Implement ArrayQueue Class
class ArrayQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._data.pop(0)

    def peek(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._data[0]

ArrayQueue = ArrayQueue()
ArrayQueue.enqueue(5)
ArrayQueue.enqueue(8)
ArrayQueue.enqueue(1)
print(ArrayQueue._data)
print('Length: ', len(ArrayQueue))
ArrayQueue.enqueue(7)
ArrayQueue.enqueue(12)
print(ArrayQueue._data)
print('Length: ', len(ArrayQueue))
i = ArrayQueue.dequeue()
print('Element removed: ', i)
print(ArrayQueue._data)
print('Length: ', len(ArrayQueue))
j = ArrayQueue.peek()
print('Element at top: ', j)