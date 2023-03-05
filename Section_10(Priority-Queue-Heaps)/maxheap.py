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

    def deletemax(self):
        if self._current_size == 0:
            print('Heap is Empty')
            return
        e = self._data[1]
        self._data[1] = self._data[self._current_size]
        self._data[self._current_size] = - 1
        self._current_size = self._current_size - 1
        parent_index = 1
        child_index = parent_index * 2
        while child_index <= self._current_size:
            if self._data[child_index] < self._data[child_index + 1]:
                child_index = child_index + 1
            if self._data[parent_index] < self._data[child_index]:
                temp = self._data[parent_index]
                self._data[parent_index] = self._data[child_index]
                self._data[child_index] = temp
                parent_index = child_index
                child_index = parent_index * 2
            else:
                break
        return e