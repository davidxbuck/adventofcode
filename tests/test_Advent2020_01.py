import networkx as nx
G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'E', weight=4)
G.add_edge('C', 'F', weight=5)
target = 'A'