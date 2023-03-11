# Graph (Abstract Data Type)
# A graph data structure is a collection of nodes that have data and are connected to other nodes.
# A graph data structure consists of a finite (and possibly mutable) set of vertices (also called nodes or points),
# together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph.
# These pairs are known as edges (also called links or lines), and for a directed graph are also known as edges but also sometimes arrows or arcs.
# The vertices may be part of the graph structure, or may be external entities represented by integer indices or references.
# A graph data structure may also associate to each edge some edge value, such as a symbolic label or a numeric attribute (cost, capacity, length,
# etc.).
#
# More precisely, a graph is a data structure (V, E) that consists of
# - A collection of vertices V
# - A collection of edges E, represented as ordered pairs of vertices (u,v)
#
# Graph Terminology
# Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them.
# Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path.
# Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well.
# The edges in such a graph are represented by arrows to show the direction of the edge.
#
# Operations
#
# The basic operations provided by a graph data structure G usually include:[1]
#
#     adjacent(G, x, y): tests whether there is an edge from the vertex x to the vertex y;
#     neighbors(G, x): lists all vertices y such that there is an edge from the vertex x to the vertex y;
#     add_vertex(G, x): adds the vertex x, if it is not there;
#     remove_vertex(G, x): removes the vertex x, if it is there;
#     add_edge(G, x, y, z): adds the edge z from the vertex x to the vertex y, if it is not there;
#     remove_edge(G, x, y): removes the edge from the vertex x to the vertex y, if it is there;
#     get_vertex_value(G, x): returns the value associated with the vertex x;
#     set_vertex_value(G, x, v): sets the value associated with the vertex x to v.
#
# Structures that associate values to the edges usually also provide:[1]
#
#     get_edge_value(G, x, y): returns the value associated with the edge (x, y);
#     set_edge_value(G, x, y, v): sets the value associated with the edge (x, y) to v.
#
# Graph ADT implemented in Python using the Adjacency List Graph Representation
# An adjacency list represents a graph as an array of linked lists.
# The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.
# Text Source: Graph Data Structure
# URL: https://www.programiz.com/dsa/graph
# Text Source: Graph (abstract data type)
# URL: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)

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

