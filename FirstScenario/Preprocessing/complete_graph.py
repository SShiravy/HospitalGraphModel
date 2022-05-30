from networkx import all_pairs_shortest_path, all_pairs_shortest_path_length
from copy import deepcopy


def complete_graph(G):
    shortest_path = dict(all_pairs_shortest_path(G))
    shortest_path_length = dict(all_pairs_shortest_path_length(G))
    complete_G = deepcopy(G)
    for i in list(shortest_path.keys()):
        for j in list(shortest_path_length[i].keys()):
            try:
                complete_G[i][j]['weight'] = shortest_path_length[i][j]
            except:
                complete_G.add_edge(i, j, weight=shortest_path_length[i][j])

    return complete_G, shortest_path, shortest_path_length
