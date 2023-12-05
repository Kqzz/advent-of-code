def input(example=False):
    if example:
        return [line.strip() for line in open("example.txt")]
    return [line.strip() for line in open("input.txt")]


checked_coords = []


def grab(matrix, x, y):
    if len(matrix) <= x or x < 0 or len(matrix[x]) <= y or y < 0:
        print("invalid coords:", x, y)
        return
    element = matrix[x][y]
    if element.isdigit():
        # search for remaining digits of number

        for i in range(1, 10):
            if y + i <= len(matrix[x]) and matrix[x][y + i].isdigit():
                element += matrix[x][y + i]
            else:
                break

        for i in range(1, 10):
            if y - i >= 0 and matrix[x][y - i].isdigit():
                element = matrix[x][y + -i] + element
            else:
                break

    return element


def adjacent_coordinates(matrix, x, y):
    coords = []

    coords.append((x, y + 1))
    coords.append((x, y - 1))
    coords.append((x + 1, y))
    coords.append((x - 1, y))
    coords.append((x + 1, y + 1))
    coords.append((x - 1, y - 1))
    coords.append((x - 1, y + 1))
    coords.append((x + 1, y - 1))


lines = input(example=True)

matrix = [list(line) for line in lines]

for row in matrix:
    print(row)

# finish up tomorrow
