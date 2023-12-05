def input(example=False):
    if example:
        return [line.strip() for line in open("example.txt")]
    return [line.strip() for line in open("input.txt")]


lines = input(example=False)


def parse_set(text):
    group = {}

    sections = [[x for x in part.split(" ") if x] for part in text.split(",")]

    for part in sections:
        group[part[-1]] = int(part[0])
    return group


class Game:
    def __init__(self, id, groups):
        self.id = id
        self.groups = groups
        self.min = {"red": 0, "blue": 0, "green": 0}


def parse_line(line):
    halves = line.split(":")

    id = int(halves[0].split(" ")[-1])

    groups = [parse_set(group) for group in halves[-1].split(";")]

    game = Game(id, groups)

    return game


games = [parse_line(line) for line in lines]

sum = 0


for game in games:
    valid = True
    for group in game.groups:
        for k, v in group.items():
            game.min.setdefault(k, v)
            if v > game.min[k]:
                game.min[k] = v

    if valid:
        product = 1
        for num in game.min.values():
            product *= num
        print(game.id, "valid", game.min, product)
        sum += product

print(sum)
