from dataclasses import dataclass


def input(example=False):
    if example:
        return [line.strip() for line in open("example.txt")]
    return [line.strip() for line in open("input.txt")]


lines = input(example=False)

numbers = []


@dataclass
class Part:
    x: int
    y: int
    part: str


@dataclass
class Number:
    x: int
    y: int
    n: int

    def __add__(self, other):
        if isinstance(other, Number):
            return self.n + other.n
        return self.n + other

    def __radd__(self, other):
        return self.n + other


def grab(matrix, x, y):
    if len(matrix) <= x or x < 0 or len(matrix[x]) <= y or y < 0:
        print("invalid coords:", x, y)
        return

    element = matrix[x][y]

    if element == ".":
        return None

    print(matrix[x])

    if element.isdigit():
        # search for remaining digits of number
        miny = y

        for i in range(1, 10):
            if y + i < len(matrix[x]) and matrix[x][y + i].isdigit():
                element += matrix[x][y + i]
            else:
                break

        for i in range(1, 10):
            if y - i >= 0 and matrix[x][y - i].isdigit():
                element = matrix[x][y - i] + element
                miny = y - i
            else:
                break

        return Number(x, miny, int(element))

    return Part(x, y, element)


def adjacent_coordinates(x, y):
    coords = []

    coords.append((x, y + 1))
    coords.append((x, y - 1))
    coords.append((x + 1, y))
    coords.append((x - 1, y))
    coords.append((x + 1, y + 1))
    coords.append((x - 1, y - 1))
    coords.append((x - 1, y + 1))
    coords.append((x + 1, y - 1))

    return coords


matrix = [list(line) for line in lines]

for x, row in enumerate(matrix):
    for y, col in enumerate(row):
        element = grab(matrix, x, y)
        if element is None:
            continue
        if type(element) is Part:
            for coord in adjacent_coordinates(x, y):
                adj = grab(matrix, *coord)
                if type(adj) is Number and adj not in numbers:
                    numbers.append(adj)

print(sum(numbers))
