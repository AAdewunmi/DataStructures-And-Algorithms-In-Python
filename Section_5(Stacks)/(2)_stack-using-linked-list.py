# Stack Abstract Data Type (ADT)
# ==============
# A stack is an Abstract Data Type (ADT), commonly used in most programming languages.
# It is named stack as it behaves like a real-world stack,
# for example – a deck of cards or a pile of plates, etc.
# A real-world stack allows operations at one end only.
# For example, we can place or remove a card or plate from the top of the stack only.
# Likewise, Stack ADT allows all data operations at one end only.
# At any given time, we can only access the top element of a stack.
# This feature makes it LIFO data structure.
# LIFO stands for Last-in-first-out. Here, the element which is placed (inserted or added) last,
# is accessed first. In stack terminology, insertion operation is called PUSH operation and removal operation is called POP operation.
#
# In Python, a stack can be implemented using either an Array or a Linked List.
# This tutorial will consider a Linked List implementation of a stack

# Node Class
class _Node:
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# Class LinkedListStack
class LinkedListStack:
    def __init__(self):
        self._top = None
        self.size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
