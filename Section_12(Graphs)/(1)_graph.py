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
# Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them. Vertices 2 and 3 are not adjacent because there is
# no edge between them.
# Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path. 0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.
# Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. The edges in such a graph are represented
# by arrows to show the direction of the edge.
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

import numpy as np

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjacent_matrix = np.array((vertices, vertices))

    def insert_edge(self, u, v, weight_edge = 1):
        self._adjacent_matrix[u][v] = weight_edge