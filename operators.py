from search import actions
from evaluation_functions import find_tile
from copy import deepcopy
from data_structures import SNode

#  Search Operators for the 8-Puzzle
def move_left(node):
    l1, l2 = find_tile(node.STATE, 0)

    if l2 == 0:
        return None
    else:
        state = deepcopy(node.STATE)
        x = state[l1][l2 - 1]
        state[l1][l2 - 1] = 0
        state[l1][l2] = x
    
    return SNode(state)

def move_right(node):
    l1, l2 = find_tile(node.STATE, 0)

    if l2 == 2:
        return None
    else:
        state = deepcopy(node.STATE)
        x = state[l1][l2 + 1]
        state[l1][l2 + 1] = 0
        state[l1][l2] = x
    
    return SNode(state)

def move_down(node):
    l1, l2 = find_tile(node.STATE, 0)

    if l1 == 2:
        return None
    else:
        state = deepcopy(node.STATE)
        x = state[l1 + 1][l2]
        state[l1 + 1][l2] = 0
        state[l1][l2] = x

    return SNode(state)

def move_up(node):
    l1, l2 = find_tile(node.STATE, 0)

    if l1 == 0:
        return None
    else:
        state = deepcopy(node.STATE)
        x = state[l1 - 1][l2]
        state[l1 - 1][l2] = 0
        state[l1][l2] = x

    return SNode(state)

# Helper for main. Placed here for ease of access to operators/actions
def instantiate_8puzzle(initial, goal):
    problem = {}

    init = SNode(initial)
    final = SNode(goal)

    problem['Initial State'] = init
    problem['Goal State'] = final
    problem['Operators'] = [move_up, move_down, move_left, move_right]
    problem['Actions'] = actions

    return(problem)

# Visualizing Functions
def print_state(node):                      # Prints given 8-puzzle state
    for x in node.STATE:
        print(x)
    print(f'Depth: {node.PATH_COST}', end = '\n\n')

def print_steps(node):                      # Prints 8-puzzle states from initial state to node's state
    x = node
    depth = node.PATH_COST
    stuff = []
    while x:
        stuff.append(x)
        x = x.PARENT

    for x in reversed(stuff):
        print_state(x)
    
