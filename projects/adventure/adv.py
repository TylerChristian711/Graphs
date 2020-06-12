from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


traversal_path = []

# UPER
"""
 we have a player that needs to move to each room in the shorest path possible 
 I will use a breadth first traversal in order to do so 
 at least two list will be needed to track what rooms have and haven't been visited by the player 
 a queue will also be need in order to keep track of what room is next to be visited 
"""


# create method for travel
def move_to_room(location):
    # this will make it simpler to move from one room to anohter
    player.travel(location)


# create method for creating a map for all rooms in the graph
def room_map():
    """
    variable to hold the current location of player and a dictionary to hold key value pairs
    """
    current_location = player.current_room

    the_map = {}


# method to find and pick a random and unvisited room in graph
def unvisited_exit_room():
    pass


# ---BFS---

# BFS method to check if rooms are visited or not

# will need to see if our visited rooms are less then the rooms in the graph
# create variable to hold our current room id to keep track of where we are

""" 
this method was tired on its own and fails the test other methods 
found above me be flushed out before we can see if this BFS would work.
"""


def traverse_graph(some_graph, start_node):
    to_visit = [start_node]  # list with one item
    visited = []  # empty list if we have not visited anything

    while to_visit:
        node_to_check = to_visit.pop(0)
        for neighbor_node in some_graph[node_to_check]:
            if neighbor_node not in visited:
                to_visit.insert(0, neighbor_node)  # put in route plan
                visited.append(neighbor_node)  # node we already added

    return visited


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
