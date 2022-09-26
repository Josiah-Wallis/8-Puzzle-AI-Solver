from data_structures import queue
from evaluation_functions import path_cost, misplaced_tile_h, manhattan_distance_h

def actions(problem, s):                                                      # Returns a list of applicable operations on state s
    avail = []
    ops = problem['Operators']

    for f in ops:
        x = f(s)

        if x is None:
            continue

        avail.append(f)

    return avail

def expand(problem, node):                                                    # Yields expanded nodes on frontier

    for action in problem['Actions'](problem, node):
        new_node = action(node)
        new_node.PATH_COST = node.PATH_COST + 1
        new_node.PARENT = node
        new_node.ACTION = action
        yield new_node

def best_first_search(problem, f):                                            # Basis for search functions
    node = problem['Initial State']
    frontier = queue()
    frontier.append(node, [f, problem])
    reached = {}
    reached[str(node.STATE)] = node                                           # Stringified states since type(node.STATE) is unhashable

    while not frontier.empty():
        node = frontier.pop()
        if problem['Goal State'] == node: return node
        for child in expand(problem, node):
            s_lookup = str(child.STATE)
            if (s_lookup not in reached) or (child.PATH_COST < reached[s_lookup].PATH_COST):
                reached[s_lookup] = child
                frontier.append(child, [f, problem])
    return 'failure'

def uniform_cost_search(problem):
    return best_first_search(problem, path_cost)

def A_star_misplaced(problem):
    return best_first_search(problem, misplaced_tile_h)

def A_star_manhattan(problem):
    return best_first_search(problem, manhattan_distance_h)