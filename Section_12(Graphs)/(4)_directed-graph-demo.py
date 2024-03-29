from graph import Graph

G = Graph(4)
G.display_adjacent_matrix()
print('Vertices:', G.vertex_count())
print('Edges:', G.edge_count())
G.edges_print()
G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,2)
G.insert_edge(2,3)
G.display_adjacent_matrix()
print('Vertices:', G.vertex_count())
print('Edges:', G.edge_count())
G.edges_print()
print('Edge 1 - 3', G.exist_edge(1,3))
print('Edge 1 - 2', G.exist_edge(1,2))
print('Indegree 2', G.indegree(2))
print('Outdegree 2', G.outdegree(2))
print('Graph Adjacency Matrix')
G.display_adjacent_matrix()
G.remove_edge(1,2)
print('Graph Adjacency Matrix')
G.display_adjacent_matrix()
print('Edges between 1--2:', G.exist_edge(1,2))