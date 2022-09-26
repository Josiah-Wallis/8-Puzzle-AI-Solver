# 8-Puzzle AI Solver
![8puzzle.jpg](https://www.dropbox.com/s/vx8xzy3z0i1he30/8puzzle.jpg?dl=0&raw=1)
An **8-puzzle** is the puzzle described above where a player moves tiles around a 3x3 grid in an attempt to **reach a predefined goal state**. In this implementation, best first search (BFS) is used to solve the 8-puzzle using three heuristics for the search tree: 
1) **Uniform Cost**: make moves based on which game states have required the least number of moves to reach thus far
2) **Misplaced Tile**: judge and make moves based on how many tiles are not in their correct goal state positions
3) **Manhattan Distance**: judge and make moves based on the taxicab distance a tile is from its goal state position

# Usage
To run the puzzle solver, simply run the `main.py` file. An example usage with outputs is provided below:
![usage.png](https://www.dropbox.com/s/tz0feda3bvhtkbr/usage.png?dl=0&raw=1)

# Results
The hardest initial puzzle state (difficulty 8 in `main.py` premade) takes 24 moves to solve if each move is optimally chosen. Using each of the three heuristics, the Manhattan Distance heuristic comes out on top as being both the quickest solver as well as the heuristic that searches the least for the solution. ![results.png](https://www.dropbox.com/s/c8n8erccff8akgk/results.png?dl=0&raw=1)
In terms of time, the Manhattan Distance heuristic improves upon misplaced tile by 94% while improving upon uniform cost search by about 96.6%. In terms of memory efficiency and nodes expanded, Manhattan Distance expands about 10% the number of nodes misplaced tile heuristic expands while expanding only 1.3% the number of nodes uniform cost search expands.

# Contact
Please send any questions, comments, or inquiries to jwall014@ucr.edu.