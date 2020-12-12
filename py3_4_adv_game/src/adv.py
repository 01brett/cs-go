import shlex
from room import room
from player import Player
from helpers import clr


moves_msg = f"{clr.bold}{clr.green}n{clr.end} north {clr.bold}{clr.green}s{clr.end} south {clr.bold}{clr.green}e{clr.end} east {clr.bold}{clr.green}w{clr.end} west {clr.bold}{clr.green}i{clr.end} inventory —— {clr.bold}{clr.green}q{clr.end} quit"
user_marker = "⏩ "


def blocked_msg(direction):
    print(f"\n{clr.fail}{direction} is blocked. Try a different direction.{clr.end}")


def error_msg(text):
    print(f"\n{clr.fail}{text}{clr.end}")


print("\nWelcome to Adventures of Los Lambdas")

print("\nPlease enter your name:")
user = input(user_marker)
player = Player(user, room["outside"])

print(f"\nHello, {clr.bold}{player.name}{clr.end}. Adventure awaits...")

print(player)

print(f"Type these characters on your keyboard to move to different rooms.")
print(moves_msg)

user = input(f"{user_marker}")


def move_player(direction):
    pretty_directions = {"n": "North", "s": "South", "e": "East", "w": "West"}
    next_room = getattr(player.current_room, str(direction) + "_to")
    if next_room is None:
        blocked_msg(pretty_directions[direction])
    else:
        player.current_room = next_room


def parse_arg(action):
    if action == "n":
        move_player(action)

    elif action == "s":
        move_player(action)

    elif action == "e":
        move_player(action)

    elif action == "w":
        move_player(action)

    elif action == "i" or action == "inventory":
        player.inventory()

    else:
        error_msg("Invalid move. Must be [n], [s], [e], [w], [i], or [q]")


def parse_args(action, item):
    if action == "get" or action == "take":
        if len(player.current_room.items) == 0:
            print(f"\n{clr.fail}No items to take.{clr.end}")
            return

        for room_item in player.current_room.items:
            if room_item.name != item:
                continue

            player.take_item(room_item)
            player.current_room.take_item(room_item)
            break

    elif action == "drop":
        if len(player.items) == 0:
            print(f"\n{clr.fail}No items to drop.{clr.end}")
            return

        for player_item in player.items:
            if player_item.name != item:
                continue

            player.current_room.drop_item(player_item)
            player.drop_item(player_item)
            break

    else:
        error_msg(
            "Invalid action. Use `get` or `take` to pickup items or `drop` to drop an item."
        )


while True:
    args = shlex.split(user)

    if len(args) == 1:
        if args[0] == "q":
            break
        parse_arg(args[0])

    if len(args) > 1:
        parse_args(args[0], args[1])

    print(player)
    user = input(f"{moves_msg}\n{user_marker}")
