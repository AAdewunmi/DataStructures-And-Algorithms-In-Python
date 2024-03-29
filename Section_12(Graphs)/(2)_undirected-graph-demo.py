from graph import Graph
# Undirected Graph Demo
G = Graph(4)
G.display_adjacent_matrix()
print('Vertices:', G.vertex_count())
print('Edges:', G.edge_count())
G.insert_edge(0, 1)
G.insert_edge(0, 2)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(2, 0)
G.insert_edge(2, 1)
G.insert_edge(2, 3)
G.insert_edge(3, 2)
G.display_adjacent_matrix()
print('Vertices:', G.vertex_count())
print('Edges:', G.edge_count())
G.edges_print()
print('Edge between 1-3', G.exist_edge(1, 3))
print('Edge between 1-2', G.exist_edge(1, 2))
print('Degree', G.indegree(2))
G.remove_edge(1,2)
print('Edge between 1-2', G.exist_edge(1, 2))