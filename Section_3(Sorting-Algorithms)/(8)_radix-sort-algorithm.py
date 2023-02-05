# Radix Sort
# ========================
# Definition: Radix sort is a sorting algorithm that sorts the elements by first grouping the individual digits of the same place value.
# Then, sort the elements according to their increasing/decreasing order.
#
# Radix Sort Complexities
# Time Complexity: O(n)
#
# Radix Sort Algorithm Pseudocode
# Algorithm radixsort(A)
#    n = length(A)
#    maxelement = max(A)
#    digits = finddigits(maxelements)
#    bins = []
#    for i = 0, i < digits, i++
#        for j = 0, j < n, j++
#            e = (A[j] / pow(10, i)) % 10
#             bins[e].append(A[j])
#        k = 0
#        for x = 0, x < 10, x++
#            A[k] = bins[x].remove()
#            k = k + 1
#
#
# Implementation
# Radix Sort in Python
def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10  # Assuming the size of the array is 10
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1

A = [63, 250, 835, 947, 651, 28]
print('Original Array: ', A)
radixsort(A)
print('Sorted Array: ', A)