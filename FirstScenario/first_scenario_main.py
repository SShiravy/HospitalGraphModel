from networkx.algorithms.approximation import christofides, asadpour_atsp, greedy_tsp
from FirstScenario.Preprocessing.complete_graph import complete_graph
from FirstScenario.Preprocessing.remove_bridge_deadend import remove_dead_end
from FirstScenario.brigit_algorithm import calculate_tour_cost, increase_costs
from creat_G_from_csv import graph_creator
from display_graph import display


def first_scenario():
    # I:\Graph_Hospital\Code\g_3_nu.csv
    # I:\Graph_Hospital\Code\complete_graph.csv

    path = "I:\Graph_Hospital\Code\g_3_nu.csv"
    G, gMatrixDataframe, gMatrix = graph_creator(path)
    display(G, 'original graph')
    # preprocessing
    remove_dead_end(G, gMatrixDataframe)
    display(G, 'preprocessed graph')
    # complete graph
    complete_G, shortest_path, shortest_path_length = complete_graph(G)
    display(complete_G, 'completed graph')
    # find tour
    path = christofides(complete_G)
    tour_cost = calculate_tour_cost(path, shortest_path_length)
    print('first tour for patients is:', path)
    # increase cost of used edges
    increase_costs(G, path, shortest_path)
    display(G, 'new graph')
    # re-complete graph
    # TODO: re-complete graph
    # TODO: Asadpour or Christofides on new complete_G

