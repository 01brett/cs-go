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


def reverse(d):
    if d == "w":
        return "e"
    if d == "n":
        return "s"
    if d == "s":
        return "n"
    if d == "e":
        return "w"
    if d == None:
        return None


visited = {}


def explore(prev_move=None):
    s = []
    room = player.current_room.id

    # add current room to visited graph if not there
    if room not in visited:
        visited[room] = {}

    # mark room we came from in visited graph
    if prev_move is not None:
        backtrack_move = reverse(prev_move)
        backtrack_room = player.current_room.get_room_in_direction(backtrack_move).id
        visited[room][backtrack_move] = backtrack_room

    adj_rooms = player.current_room.get_exits()

    # add to stack the adj_rooms of our current room
    for next_move in adj_rooms:
        if next_move not in visited[room]:
            visited[room][next_move] = "?"

        adj_room = player.current_room.get_room_in_direction(next_move).id

        # if we haven't been to next room or that move is unexplored, add to stack
        if adj_room not in visited or visited[room][next_move] == "?":
            s.append(next_move)

    # loop over the stack of rooms to visit
    while len(s) > 0:
        move = s.pop()
        next_room = player.current_room.get_room_in_direction(move).id

        # skip loop iter if we've been to room
        if next_room in visited:
            continue

        # mark the move in our path arr
        traversal_path.append(move)
        # mark room in our visited graph
        visited[player.current_room.id][move] = next_room
        # move our player
        player.travel(move)

        # recursion!
        explore(move)

        if len(visited) == len(room_graph):
            return
        # if we reach this code, we've backed out of our recursion
        # get the opposite of the move we recursed with
        backtrack = reverse(move)
        # add the backtrack to our path
        traversal_path.append(backtrack)
        # move our player in backtrack direction
        player.travel(backtrack)


explore()

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
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
