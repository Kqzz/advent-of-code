base_input = open("input.txt").readlines()

x, y, aim = 0, 0, 0

for movement in base_input:
    movement = movement.split(" ")
    op = movement[0]
    val = int(movement[1])

    if op == "down":
        aim += val
    elif op == "up":
        aim -= val
    elif op == "forward":
        x += val
        y += aim * val

print(f"part two solution: {x * y}")

