# Finding the shortest path with an energy budget

In this project, we take the problem instance of the New York City road network to find the shortest path between a source node and a goal node. This instance is modified from the 9th DIMACS implementation challenge, and contains 264346 nodes and 730100 edges.

## Information provided
Graph dictionary G: The graph is given as an adjacency list where the neighbor list of node ‘v’ can be accessed with G[‘v’].
Node coordination dictionary Coord: The coordination of a node ‘v’ is a pair (X, Y) which can be accessed with Coord[‘v’].
Edge distance dictionary Dist: The distance between a pair of node (v, w) can be accessed with Dist[‘v,w’].
Edge cost dictionary Cost: The energy cost between a pair of node (v, w) can be accessed with Cost[‘v,w’.].

## Tasks
The problem can be split into three tasks in order as follows.
Task 1: A relaxed version of the NYC instance where we do not have the energy constraint. This is equivalent to solving the shortest path problem.
Task 2: Implementation of an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance.
Task 3: Development of an A* search algorithm to solve the NYC instance. The key is to develop a suitable heuristic function for the A* search algorithm in this setting.

For tasks 2 and 3, the energy budget is set to be 287932. For all the 3 tasks, the starting and ending nodes are set to be ‘1’ and ‘50’, respectively.
