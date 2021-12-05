# modules and dependencies
from functions import *

# open json files and convert into python dicts
with open("G.json") as g_json:
    g_dict = json.load(g_json)
with open("Coord.json") as coord_json:
    coord_dict = json.load(coord_json)
with open("Dist.json") as dist_json:
    dist_dict = json.load(dist_json)
with open("Cost.json") as cost_json:
    cost_dict = json.load(cost_json)

energy_budget = 287932
start = 1
goal = 50

# TASK 1
print("================== TASK 1 ==================")
# find shortest path using UCS
# nodes are ordered using path cost g(n)
# use g, dist
ucs(g_dict, start, goal, dist_dict)


# TASK 2
print("================== TASK 2 ==================")
# find shortest path using UCS
# nodes are ordered using path cost g(n)
# use g, dist, cost
# include a check at every iteration to make sure total energy cost has not exceeded constraint
# if exceeded, don't add node to frontier
ucs_with_energy_constraint(g_dict, start, goal, dist_dict, cost_dict, energy_budget)


# TASK 3
print("================== TASK 3 ==================")
# find shortest path using A* search
# nodes are ordered using f(n) = g(n) + h(n)
# use g, dist, cost, coord
# include a check at every iteration to make sure total energy cost has not exceeded constraint
# if exceeded, don't add node to frontier
# for heuristic function h(n), find straight-line distance between node and goal node
a_star(g_dict, start, goal, dist_dict, cost_dict, energy_budget, coord_dict)

