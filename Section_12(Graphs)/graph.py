from queuelinkedlist import LinkedListQueue
import numpy as np

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjacent_matrix = np.zeros((vertices, vertices))
        self._visited = [0] * self._vertices

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

    def BFS(self, source_vertex):
        i = source_vertex
        q = LinkedListQueue()

        print(i, end=' ')
        self._visited[i] = 1
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjacent_matrix[i][j] == 1 and self._visited[j] == 0:
                    print(j, end=' ')
                    self._visited[j] = 1
                    q.enqueue(j)

    def DFS(self,source_vertex):
        if self._visited[source_vertex]==0:
            print(source_vertex,end=' ')
            self._visited[source_vertex]=1
            for j in range(self._vertices):
                if self._adjacent_matrix[source_vertex][j]==1 and self._visited[j]==0:
                    self.DFS(j)