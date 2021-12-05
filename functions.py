# modules and dependencies
import json
import math
from queue import PriorityQueue

# open json files and convert into python dicts
with open("G.json") as g_json:
    g_dict = json.load(g_json)
with open("Coord.json") as coord_json:
    coord_dict = json.load(coord_json)
with open("Dist.json") as dist_json:
    dist_dict = json.load(dist_json)
with open("Cost.json") as cost_json:
    cost_dict = json.load(cost_json)

# heuristic function
def h(n, goal, coord):

    # obtain coordinates of goal and current nodes
    goal_x = coord[str(goal)][0]
    goal_y = coord[str(goal)][1]
    cur_x = coord[str(n)][0]
    cur_y = coord[str(n)][1]

    # find pythagorean distance between goal state node and current node n
    x_diff = goal_x - cur_x
    y_diff = goal_y - cur_y
    pydist = math.sqrt(x_diff ** 2 + y_diff ** 2)

    # return pythagorean distance as heuristic
    return pydist

# function to find path cost between two nodes
def find_distance(node1, node2, dist):
    key = str(node1) + "," + str(node2)
    return dist[key]

# function to find energy cost between two nodes
def find_energy_cost(node1, node2, cost):
    key = str(node1) + "," + str(node2)
    return cost[key]

# function to print path
def iter_print_path(parent, j):
    path_list = []
    path_list.insert(0, j)
    while parent[j-1] != -1:
        path_list.insert(0, parent[j-1])
        j = parent[j-1]
    return path_list

# TASK 1
def ucs(graph, start, goal, dist):
    # create array to store parent nodes
    parent = []
    for i in range(len(graph)):
        parent.append(-1)

    # create a priority queue
    frontier = PriorityQueue()
    # insert start node into priority queue
    frontier.put((0, start))

    # create array to store visited nodes
    visited = []

    # create array to store path costs
    distances = []
    for i in range(len(graph)):
        distances.append(math.inf)

    while True:

        # if no nodes to visit next, exit loop
        if frontier.empty():
            break

        # pop the top element in queue
        (weight, current_node) = frontier.get()
        distances[int(current_node)-1] = weight

        # mark current node as visited
        visited.append(current_node)

        # if we have reached the goal node, return
        if int(current_node) == goal:
            break

        # if we have not reached the goal node,
        # consider neighbours of current node
        for neighbour in graph[str(current_node)]: # neighbour is a str
            if neighbour not in visited:
                distance = find_distance(current_node, neighbour, dist)
                old_dist = distances[int(neighbour)-1]
                new_dist = weight + distance
                if new_dist < old_dist:
                    frontier.put((new_dist, neighbour))
                    distances[int(neighbour)-1] = new_dist
                    parent[int(neighbour)-1] = int(current_node)

    print("Shortest path:", end=" ")
    print(*iter_print_path(parent, goal), sep="->")
    print("Shortest distance:", distances[goal-1])

# TASK 2
def ucs_with_energy_constraint(graph, start, goal, dist, cost, budget):
    # create array to store parent nodes
    parent = []
    for i in range(len(graph)):
        parent.append(-1)

    # create a priority queue
    frontier = PriorityQueue()
    # insert start node into priority queue
    frontier.put((0, start))

    # create array to store visited nodes
    visited = []

    # create array to store path distances
    distances = []
    for i in range(len(graph)):
        distances.append(math.inf)

    # create array to store energy costs
    costs = []
    for i in range(len(graph)):
        costs.append(0)

    while True:

        # if no nodes to visit next, exit loop
        if frontier.empty():
            break

        # pop the top element in queue
        (weight, current_node) = frontier.get()
        distances[int(current_node)-1] = weight

        # mark current node as visited
        visited.append(current_node)

        # if we have reached the goal node, return
        if int(current_node) == goal:
            break

        # if we have not reached the goal node,
        # consider neighbours of current node
        for neighbour in graph[str(current_node)]: # neighbour is a str
            if neighbour not in visited:
                distance = find_distance(current_node, neighbour, dist)
                old_dist = distances[int(neighbour)-1]
                new_dist = weight + distance
                if new_dist < old_dist:
                    energy_cost = find_energy_cost(current_node, neighbour, cost)
                    new_cost = energy_cost + costs[int(current_node)-1]
                    if new_cost > budget:
                        continue
                    else:
                        frontier.put((new_dist, neighbour))
                        distances[int(neighbour)-1] = new_dist
                        parent[int(neighbour)-1] = int(current_node)
                        costs[int(neighbour)-1] = new_cost

    print("Shortest path:", end=" ")
    print(*iter_print_path(parent, goal), sep="->")
    print("Shortest distance:", distances[goal-1])
    print("Total energy cost:", costs[goal-1])

# TASK 3
def a_star(graph, start, goal, dist, cost, budget, coord):
    # create array to store parent nodes
    parent = []
    for i in range(len(graph)):
        parent.append(-1)

    # create a priority queue
    frontier = PriorityQueue()
    # insert start node into priority queue
    frontier.put((h(start, goal, coord), start))

    # create array to store visited nodes
    visited = []

    # create array to store path distances
    distances = []
    for i in range(len(graph)):
        distances.append(math.inf)
    distances[int(start)-1] = 0

    # create array to store energy costs
    costs = []
    for i in range(len(graph)):
        costs.append(0)

    while True:

        # if no nodes to visit next, exit loop
        if frontier.empty():
            break

        # pop the top element in queue
        (weight, current_node) = frontier.get()

        # mark current node as visited
        visited.append(current_node)

        # if we have reached the goal node, return
        if int(current_node) == goal:
            break

        # if we have not reached the goal node,
        # consider neighbours of current node
        for neighbour in graph[str(current_node)]: # neighbour is a str
            if neighbour not in visited:
                distance = find_distance(current_node, neighbour, dist)
                new_dist = distances[int(current_node)-1] + distance
                heuristic = h(neighbour, goal, coord)
                f = new_dist + heuristic
                old_dist = distances[int(neighbour)-1]
                if new_dist < old_dist:
                    energy_cost = find_energy_cost(current_node, neighbour, cost)
                    new_cost = energy_cost + costs[int(current_node)-1]
                    if new_cost > budget:
                        continue
                    else:
                        frontier.put((f, neighbour))
                        distances[int(neighbour)-1] = new_dist
                        parent[int(neighbour)-1] = int(current_node)
                        costs[int(neighbour)-1] = new_cost

    print("Shortest path:", end=" ")
    print(*iter_print_path(parent, goal), sep="->")
    print("Shortest distance:", distances[goal-1])
    print("Total energy cost:", costs[goal-1])
