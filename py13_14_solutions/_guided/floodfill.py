img_str = [
    "|----------------------------------------|",
    "|                                        |",
    "|         ||||||||||||||||               |",
    "|        |    |           |              |",
    "|       |    | |          |              |",
    "|       |    | |         |               |",
    "|       |    | |     ||||                |",
    "|       |     |     |                    |",
    "|        |         |                     |",
    "|         |       |                      |",
    "|          |||||||                       |",
    "|                                        |",
    "|                             |||        |",
    "|                             | |        |",
    "|                           |||  |||     |",
    "|                           |      |     |",
    "|                           |||  |||     |",
    "|                              ||        |",
    "|----------------------------------------|",
]
image = []
for i in img_str:
    image.append(list(i))


def print_img():
    for i in image:
        print("".join(i))


def floodfill(row, col, char):
    if image[row][col] != " ":
        return

    image[row][col] = char

    floodfill(row, col + 1, char)  # move right
    floodfill(row, col - 1, char)  # move left
    floodfill(row + 1, col, char)  # move down
    floodfill(row - 1, col, char)  # move up


floodfill(5, 12, "·")
floodfill(2, 2, "^")

print_img()
