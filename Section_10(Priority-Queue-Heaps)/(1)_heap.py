# Priority Queue (Abstract Data Type)
# In computer science, a priority queue is an abstract data-type similar to a regular queue or stack data structure.
# Each element is a priority queue has an associated priority. In a priority queue, elements with high priority are
# served before elements with low priority. In some implementations, if two elements have the same priority, they are
# served in the same order that they were enqueued in. In other implementations, the order of elements with the same
# priority is undefined.
#
# Implementation:
# While priority queues are often implemented using heaps, they are conceptually distinct from heaps.
# A priority queue is an abstract data structure like a list or a map; just as a list can be implemented with
# a linked list or with an array, a priority queue can be implemented with a heap or another method such as an
# unordered array. To improve performance, priority queues are typically based on a heap, giving O(log n) performance
# for inserts and removals, and O(n) to build the heap initially from a set of n elements.
# Variants of the basic heap data structure such as pairing heaps or Fibonacci heaps can provide better bounds for some
# operations.
#
# Text Source: Priority queue
# URL: https://en.wikipedia.org/wiki/Priority_queue
#
# Heap
# Heap data structure is a complete binary tree that satisfies the heap property, where any given node is:
# (a) always greater than its child node(s) and the key of the root node is the largest among all other nodes.
# This property is called the Max Heap property.
# (b) always smaller than the child node(s) and the key of the root node is the smallest among all other nodes.
# This property is called Min Heap property.
#
# Heap Operations
# Heapify: Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.
# Insert Element into Heap
# Delete Element from Heap
# Peek (Find max/min): Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.
# Extract-Max/Min: Extract-Max returns the node with maximum value after removing it from a Max Heap whereas Extract-Min returns the node
# with minimum after removing it from Min Heap.
#
# Text Source: Programiz
# Title: Heap Data Structure
# URL: https://www.programiz.com/dsa/heap-data-structure
#
# Array based implementation of Heap
class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1] * self._maxsize
        self._current_size = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)

    def insert(self, e):
        if self._current_size == self._maxsize:
            print('No Space in Heap')
            return
        self._current_size = self._current_size + 1
        insert_index = self._current_size
        while insert_index > 1 and e > self._data[insert_index//2]:
            self._data[insert_index] = self._data[insert_index//2]
            insert_index = insert_index//2
        self._data[insert_index] = e

    def max(self):
        if self._current_size == 0:
            print('No space in heap')
            return
        return self._data[1]

S= Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
print(S._data)