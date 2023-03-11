from queuelinkedlist import LinkedListQueue
import numpy as np

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjacent_matrix = np.zeros((vertices, vertices))

    def insert_edge(self, u, v, weight_edge = 1):
        self._adjacent_matrix[u][v] = weight_edge

    def remove_edge(self, u, v):
        self._adjacent_matrix[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjacent_matrix[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjacent_matrix[i][j] != 0:
                    count = count + 1
        return count

    def vertices_print(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges_print(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjacent_matrix[i][j] != 0:
                    print(i, '--', j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if not self._adjacent_matrix[v][j] != 0:
                count = count + 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjacent_matrix[i][v] != 0:
                count = count + 1
        return count

    # Helper function to display adjacency matrix
    def display_adjacent_matrix(self):
        print(self._adjacent_matrix)