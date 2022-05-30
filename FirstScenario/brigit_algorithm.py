from config import INCREASE_RATE


def calculate_tour_cost(path, shortest_path_length):
    tour_cost = 0
    for i in range(len(path) - 1):
        tour_cost += shortest_path_length[path[i]][path[i + 1]]
    return tour_cost


def increase_costs(G, path, shortest_path):
    maximum_weight = max(dict(G.edges).items(), key=lambda x: x[1]['weight'])[1]['weight']

    def increase(path):
        for i in range(len(path) - 1):
            try:
                G[path[i]][path[i + 1]]['weight'] = maximum_weight + INCREASE_RATE
                print(path[i], '-->', path[i + 1])
            except:
                print(f'there is no edge between {path[i]} and {path[i + 1]} in original graph \n '
                      f'this virtual edge equivalent to: {shortest_path[path[i]][path[i + 1]]}')
                increase(shortest_path[path[i]][path[i + 1]])

    increase(path)
