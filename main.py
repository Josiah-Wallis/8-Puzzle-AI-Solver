from search import uniform_cost_search, A_star_misplaced, A_star_manhattan
from operators import instantiate_8puzzle, print_state, print_steps
from timeit import default_timer

# Hardcoded as goal state will be the same for each run
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Choose a custom or premade state, using premade states from project description
def puzzle_init_state():
    while True:
        print('Welcome to my 8-Puzzle Solver!')
        response = input('Would you like a custom or premade setup? (custom/premade): ')

        if((response != 'custom') and (response != 'premade')):
            print('Invalid response!', end = '\n\n')
            continue
        
        print()
        break

    if response == 'custom':
        print('Please enter each row as a space-separated list! For example: 1 2 3')
        r1 = input('Row 1: ')
        r2 = input('Row 2: ')
        r3 = input('Row 3: ')

        matrix = []
        for x in [r1, r2, r3]:
            a, b, c = int(x[0]), int(x[2]), int(x[4])
            row = [a, b, c]
            matrix.append(row)
        
    else:
        print('I have a selection of 8 premade initial states for you!')
        selection = int(input('On a difficulty scale from 1 to 8, 1 being easy and 8 being very hard,\nwhich would you like to solve? '))
        print()

        if selection == 1:
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif selection == 2:
            matrix = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        elif selection == 3:
            matrix = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
        elif selection == 4:
            matrix = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
        elif selection == 5:
            matrix = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
        elif selection == 6:
            matrix = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
        elif selection == 7:
            matrix = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
        elif selection == 8:
            matrix = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]

    print('Initial State: ')
    for x in matrix:
        print(x)
    print()

    print('Goal State: ')
    for x in GOAL_STATE:
        print(x)
    print()

    return(matrix)

def timed_function(func, problem):                                       # Wrapper to time search functions 
    start = default_timer()
    solution = func(problem)
    end = default_timer()

    return [end - start, solution]

def format_result(x):                                                    # Dynamically format the time search took to find solution
    to_format = str(x).split('.')                                        # Formats to 3 nonzero digits after the decimal

    if to_format[1][-3] == '-':
        zeros = int(to_format[1][-1])
        zeros += 3
        formatted = round(x, zeros)
    else:
        for index, char in enumerate(to_format[1]):
            if  char != '0':
                break
        
        formatted = round(x, index + 3)

    return formatted

def main():
    init_state = puzzle_init_state()
    problem = instantiate_8puzzle(init_state, GOAL_STATE)

    search_choice = int(input('Which search would you like to attempt to find the solution? (1/2/3):\n\t1) Uniform Cost Search\n\t2) A* with the Misplaced Tile Heuristic\n\t3) A* with the Manhattan Distance Heuristic\nYour choice: '))
    
    if search_choice == 1:
        results = timed_function(uniform_cost_search, problem)
        alg = 'Uniform Cost Search'
    elif search_choice == 2:
        results = timed_function(A_star_misplaced, problem)
        alg = 'A* with the Misplaced Tile heuristic'
    elif search_choice == 3:
        results = timed_function(A_star_manhattan, problem)
        alg = 'A* with the Manhattan Distance heuristic'

    print('\nPath from initial state to goal state:')
    print_steps(results[1])
    print(alg + f' took about {format_result(results[0])} seconds to find the solution!') 
    
if __name__ == '__main__':
    main()
