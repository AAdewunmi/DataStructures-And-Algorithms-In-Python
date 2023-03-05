from maxheap import Heap

def HeapMinSort(A):
    H = Heap()
    length_list = len(A)
    for i in range(length_list):
        H.insert(A[i])
    index_list = length_list - 1
    for i in range(H._current_size):
        A[index_list] = H.deletemax()
        index_list -= 1

A= [63, 250, 835, 947, 651, 28]
print('Original List: ', A)
HeapMinSort(A)
print('Min Sorted List: ', A)