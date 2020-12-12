# Write a class to hold player information, e.g. what room they are in
# currently.
from typing import List
from room import Room
from item import Item
from helpers import clr


class Player:
    def __init__(self, name: str, current_room: Room, items: List[Item] = []) -> None:
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self) -> str:
        return f"\n{self.current_room}\n"

    def inventory(self) -> None:
        inv = f"\n{clr.bold}{clr.green}Inventory:{clr.end}"
        if len(self.items) > 0:
            for item in self.items:
                inv += " " + item.name
        else:
            inv += " [Empty]"

        print(f"{inv}")

    def take_item(self, item: Item) -> None:
        self.items.append(item)

    def drop_item(self, item: Item) -> None:
        self.items.remove(item)
