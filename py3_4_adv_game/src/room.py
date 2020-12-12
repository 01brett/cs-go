# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item
from helpers import clr
import textwrap

wrapper = textwrap.TextWrapper(width=60)


class Room:
    def __init__(self, name: str, description: str, items: List[Item] = []) -> None:
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self) -> str:
        location = clr.bold + "Location: " + clr.end + clr.cyan + self.name + clr.end

        desc = wrapper.fill(text=self.description)

        inv = f"\n{clr.bold}Items:{clr.end}"
        if len(self.items) > 0:
            for item in self.items:
                inv += " " + item.name
        else:
            inv = ""

        return f"{location}{inv}\n{desc}"

    def take_item(self, item):
        item.on_take()
        self.items.remove(item)

    def drop_item(self, item):
        item.on_drop()
        self.items.append(item)


store = {
    "coins": Item("coins", "bleep bloop blurp"),
    "sword": Item("sword", "bleep bloop blurp"),
    "shield": Item("shield", "bleep bloop blurp"),
    "meat": Item("meat", "bleep bloop blurp"),
    "potion": Item("potion", "bleep bloop blurp"),
    "manna": Item("manna", "bleep bloop blurp"),
    "daggar": Item("daggar", "bleep bloop blurp"),
}

room = {
    "outside": Room(
        "Outside Cave Entrance",
        """North of you, the cave mount beckons""",
        [store["meat"]],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
        [store["coins"], store["manna"], store["daggar"]],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
        [store["shield"]],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
        [store["coins"]],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
        [store["coins"], store["potion"], store["manna"], store["sword"]],
    ),
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]
