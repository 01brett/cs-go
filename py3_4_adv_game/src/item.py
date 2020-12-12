from helpers import clr


class Item:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def on_take(self) -> None:
        print(f"\nYou have picked up {clr.bold}{self.name}{clr.end}.")

    def on_drop(self) -> None:
        print(f"\nYou have dropped {clr.bold}{self.name}{clr.end}.")
