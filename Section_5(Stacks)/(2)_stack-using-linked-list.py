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
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# Class LinkedListStack
class LinkedListStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element, None)
        if self.is_empty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end=' --> ')
            p = p._next
        print()

linkedlist_stack = LinkedListStack()
linkedlist_stack.push(5)
linkedlist_stack.push(7)
linkedlist_stack.push(9)
print('Push Element:')
linkedlist_stack.display()
print('Stack Length:', len(linkedlist_stack))
print('Pop Element:', linkedlist_stack.pop())
print('Push Element:')
linkedlist_stack.display()
print('Stack Length:', len(linkedlist_stack))
print('Top Element:', linkedlist_stack.top())