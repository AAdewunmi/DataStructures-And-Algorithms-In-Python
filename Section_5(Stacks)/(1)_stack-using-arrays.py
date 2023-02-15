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
# This tutorial will consider an Array implementation of a stack


# StackArray Class
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0