heart = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]


def rotate_grid(grid, turns=0):
    """
    prints grid clockwise rotated by turns
    """

    rows = len(grid)
    cols = len(grid[0])

    moves = [
        {
            "xa": 0,
            "xb": rows,
            "xi": 1,
            "ya": 0,
            "yb": cols,
            "yi": 1,
            "a": True,
        },
        {
            "xa": 0,
            "xb": cols,
            "xi": 1,
            "ya": rows - 1,
            "yb": -1,
            "yi": -1,
            "a": False,
        },
        {
            "xa": 0,
            "xb": rows,
            "xi": 1,
            "ya": cols - 1,
            "yb": -1,
            "yi": -1,
            "a": True,
        },
        {
            "xa": cols - 1,
            "xb": -1,
            "xi": -1,
            "ya": 0,
            "yb": rows,
            "yi": 1,
            "a": False,
        },
    ]

    mv = moves[turns % 4]

    for x in range(mv["xa"], mv["xb"], mv["xi"]):
        for y in range(mv["ya"], mv["yb"], mv["yi"]):
            if mv["a"]:
                print(grid[x][y], end="")
            else:
                print(grid[y][x], end="")
        print()


# print(0)
# rotate_grid(heart, 0)
# print(3)
# rotate_grid(heart, 3)
# print(4)
# rotate_grid(heart, 4)
