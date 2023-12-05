base_input = open("input.txt").readlines()

def parse_mv(mv_str):
    movement = mv_str.split(" ")

    mv = {
            "forward": [1, 0],
            "up": [0, -1],
            "down": [0, 1]
    }[movement[0]]

    mv[0] *= int(movement[1])
    mv[1] *= int(movement[1])

    return mv


commands = [parse_mv(mv) for mv in base_input]

pos = [0, 0]

for mv in commands:
    pos[0] += mv[0]
    pos[1] += mv[1]

    print(pos)

print(f"part one answer: {pos[0] * pos[1]}")
