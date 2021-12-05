# modules and dependencies
import json
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

# TASK 1
# find shortest path using UCS
# use g, dist
# complete, optimal


# TASK 2
# find shortest path using UCS
# use g, dist, cost
# complete, optimal
# implement UCS algorithm but include a check at every iteration
# to make sure total energy cost has not exceeded constraint
# if exceeded, pop from front of queue and move to next node in queue


# TASK 3
# uses A* search
# f(n) = g(n) + h(n)
# use g, dist, cost, coord
# for g(n), use priority queue implementation to add successive path costs
# use coord to find h(n), create heuristic function


