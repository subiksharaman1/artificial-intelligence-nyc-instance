# modules and dependencies
import json
import math

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
def h(n):

    # goal state is fixed: node 50 = [-73643471, 41026897]
    goal_x = coord_dict["50"][0]
    goal_y = coord_dict["50"][1]
    cur_x = coord_dict[n][0]
    cur_y = coord_dict[n][1]

    # find pythagorean distance between goal state node and current node n
    x_diff = goal_x - cur_x
    y_diff = goal_y - cur_y
    pydist = math.sqrt(x_diff ** 2 + y_diff ** 2)

    # return pythagorean distance as heuristic
    return pydist

def UCS():
