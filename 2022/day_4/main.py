"""
solution for advent of code day 5 2022
"""

original_data = [line.rstrip() for line in open(
    'input.txt', 'r', encoding="UTF-8").readlines()]


def parse_stacks(data):
    """ACction"""

    base_stacks = data[0:data.index('')-1][::-1]
    stacks = [[], [], [], [], [], [], [], [], []]

    for line in base_stacks:  # each line
        for (index, position) in enumerate(range(0, len(line), 4)):
            section = line[position:position+4]
            if not any([c.isalpha() for c in section]):
                continue
            stacks[index].append(section[1])

    return stacks


def parse_actions(stacks: list, actions: list):
    """DO thigns"""
    for action in actions:
        spl = action.split(" ")
        if len(spl) < 2:
            continue
        count = int(spl[1])
        fro = int(spl[3]) - 1
        tox = int(spl[-1]) - 1

        for _ in range(count):
            stacks[tox].append(stacks[fro].pop())

    tops = []
    for stack in stacks:
        tops.append(stack[-1])
    return tops


def parse_actions_part_two(stacks: list, actions: list):
    """DO thigns"""
    for action in actions:
        spl = action.split(" ")
        if len(spl) < 2:
            continue
        count = int(spl[1])
        fro = int(spl[3]) - 1
        tox = int(spl[-1]) - 1


        to_append = []
        for _ in range(count):
            to_append.append(stacks[fro].pop())

        for item in to_append[::-1]:
            stacks[tox].append(item)

    tops = []
    for stack in stacks:
        tops.append(stack[-1])
    return tops


parsed_stacks = parse_stacks(original_data)
final_tops = parse_actions(
    parsed_stacks, original_data[original_data.index(''):])

print("Part One", "".join(final_tops))


parsed_stacks = parse_stacks(original_data)
final_tops = parse_actions_part_two(
    parsed_stacks, original_data[original_data.index(''):])

print("Part Two", "".join(final_tops))
