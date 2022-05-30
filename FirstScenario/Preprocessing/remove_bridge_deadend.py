import networkx as nx


def remove_dead_end(G, gMartix):
    n_nodes = G.number_of_nodes()
    bridges_dead_ends = list(nx.bridges(G))
    dead_ends = {}  # from node in key to dead end node in value
    for n1, n2 in bridges_dead_ends:
        if list(gMartix[n1]).count(-1) == n_nodes-1:
            G.remove_node(n1)
            dead_ends[n2] = n1
        elif list(gMartix[n2]).count(-1) == n_nodes-1:
            G.remove_node(n2)
            dead_ends[n1] = n2
    return dead_ends
