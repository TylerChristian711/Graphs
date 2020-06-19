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
graph_map = {}
visited_rooms_map = []

# UPER
"""
 we have a player that needs to move to each room in the shorest path possible 
 I will use a breadth first traversal in order to do so 
 at least two list will be needed to track what rooms have and haven't been visited by the player 
 a queue will also be need in order to keep track of what room is next to be visited 
"""


# this fucntion is linking the exits of our rooms to each other
def direction_links(direction):
    if direction == 'n':
        # return the opposite direction in order to get our exit
        return 's'

    elif direction == 's':
        return 'n'

    elif direction == 'e':
        return 'w'

    elif direction == 'w':
        return 'e'
    else:
        return "your input has caused some error with the direction_link function"


graph_map[player.current_room] = player.current_room.get_exits()
print('room exits:', graph_map[player.current_room])
 # when the number of rooms in room_graph are less then the graph itself we want to traverse, and remove the current room
 # so we don't count it more than once
while len(graph_map) < len(room_graph) - 1:
     # checking if the our current room has already been visited
    if player.current_room not in graph_map:
        # set the list of exits to be our current room
        graph_map[player.current_room] = player.current_room.get_exits()
        # mark the room we just visited by adding the direction from the room to our list of visited rooms
        prevous_room = visited_rooms_map[-1]

        # check current path we are moving on for any dead ends
    while len(graph_map[player.current_room]) < 1:
        # remove the last direction from our dictionary so we wont move threw it again
        last_direction = visited_rooms_map.pop()

        # move back from the rooms
        player.travel(last_direction)
        # add the path to the paths that we have traveled in
        traversal_path.append(last_direction)
    else:
        # check if there any rooms we have not explored yet
        # remove the last direction
        exit = graph_map[player.current_room].pop()

        # link the exit then save our exit to our traversal_path
        traversal_path.append(exit)

        visited_rooms_map.append(direction_links(exit))
        # moving to the next room
        player.travel(exit)



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
