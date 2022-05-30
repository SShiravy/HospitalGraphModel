import networkx as nx
import pandas as pd
from config import complete_graph, nodes_name


def test_with_complete_graph():
    gMatrixDataframe = pd.DataFrame(data=complete_graph,
                                    index=nodes_name,
                                    columns=nodes_name)
    G = nx.Graph()
    G.add_nodes_from(nodes_name)
    length = len(complete_graph)
    for row in range(length):
        for i in range(length):
            if complete_graph[row][i] != -1:
                G.add_weighted_edges_from([(nodes_name[row], nodes_name[i], complete_graph[row][i])])

    return G, gMatrixDataframe, complete_graph
