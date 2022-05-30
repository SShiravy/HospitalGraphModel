import matplotlib.pyplot as plt
import networkx as nx


def display(G,title):
    pos = nx.spring_layout(G)
    cost = dict([( (u,v), d['weight']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=cost)
    nx.draw_networkx_nodes(G, pos, node_color='g')
    plt.title(title)
    plt.show()
