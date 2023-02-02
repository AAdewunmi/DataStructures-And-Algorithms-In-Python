# Bubble Sort Algorithm
# ========================
# Definition: Bubble sort is a sorting algorithm that compares adjacent elements
# and swaps them until they are in the intended order.
#
# Bubble Sort Complexity
# O(n2)
#
# Bubble Sort Algorithm
# Algorithm bubble-sort(A)
#   n = length(A)
#   for pass = n - 1, pass >= 0, pass--
#       for i = 0, i < pass, i++
#            if A[i] > A[i + 1] then
#                  temp = A[i]
#                  A[i] = A[i + 1]
#                  A[i + 1] = temp
#
# Bubble Sort Algorithm Implementation
def bubblesort(A):
    n = len(A)
    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp


A = [3, 5, 8, 9, 6, 2]
print(A)
bubblesort(A)
print(A)