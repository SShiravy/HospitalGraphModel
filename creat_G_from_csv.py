import numpy as np
import pandas as pd
import networkx as nx


def graph_creator(path):
    gMatrixDataframe = pd.read_csv(path)
    gMatrix = np.array(gMatrixDataframe)
    nodes = list(gMatrixDataframe.columns)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    length = len(gMatrix)
    for row in range(length):
        for i in range(length):
            if gMatrix[row][i] != -1:
                G.add_weighted_edges_from([(nodes[row], nodes[i], gMatrix[row][i])])

    return G, gMatrixDataframe, gMatrix


