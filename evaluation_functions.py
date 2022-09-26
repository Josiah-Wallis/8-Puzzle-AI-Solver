# Helper Function
def find_tile(state, val):                          # Returns the array position of tile val in 8-puzzle defined by state
    for x in range(len(state)):
        for y in range(len(state)):
            if state[x][y] == val:
                return (x, y)

# Evaluation Functions
def path_cost(node, problem):                       # Returns number of edges from initial state to self.STATE
    return node.PATH_COST

def misplaced_tile_h(node, problem):                # Misplaced Tile Heuristic + Path Cost
    goal = problem['Goal State']                    # Sums the number of current state tiles that mismatch with goal state tiles
    counter = 0

    for x in range(len(node.STATE)):
        for y in range(len(node.STATE)):
            if goal.STATE[x][y] != node.STATE[x][y]:
                counter += 1

    return counter + node.PATH_COST

def manhattan_distance(p1, p2):                     # Manhattan Distance
    term1 = abs(p1[0] - p2[0])
    term2 = abs(p1[1] - p2[1])

    return term1 + term2

def manhattan_distance_h(node, problem):            # Manhattan Distance Heuristic + Path Cost
    goal = problem['Goal State']                    # Sums manhattan distances from current tile locations to goal tile locations
    counter = 0

    for x in range(len(node.STATE)):                
        for y in range(len(node.STATE)):
            tile = node.STATE[x][y]         
            
            #if 0 < tile < 9:
            #    counter += manhattan_distance((x, y), find_tile(goal.STATE, tile))        

            if tile == 1:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 1))
            elif tile == 2:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 2))
            elif tile == 3:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 3))
            elif tile == 4:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 4))
            elif tile == 5:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 5))
            elif tile == 6:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 6))
            elif tile == 7:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 7))
            elif tile == 8:
                counter += manhattan_distance((x, y), find_tile(goal.STATE, 8))
            else:
                continue
            

    return counter + node.PATH_COST
