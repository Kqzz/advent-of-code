base_input = open("input.txt").readlines()

depths = [int(depth) for depth in base_input]

def part_one():
    increments = 0

    for (i, depth) in enumerate(depths):
        if depth > depths[i - 1]:
            increments += 1

    print(f"increments: {increments}")

def part_two():
    increments = 0

    for (i, depth) in enumerate(depths):
        try:
            if depth + depths[i - 1] + depths[i - 2] > depths[i - 1] + depths[i - 2] + depths[i - 3]:
                increments += 1
        except Exception:
            pass
    

    print(increments)

part_two()
