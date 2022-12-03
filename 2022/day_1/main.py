data = [l.strip().split(" ")
        for l in open("input.txt", "r", encoding="UTF-8").readlines()]

op_choices = {
    "A": 1,
    "B": 2,
    "C": 3,
}

choices = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def compute_win(you, op):
    if you == op:
        return 3
    you -= 1
    you = 3 if you == 0 else you
    if you == op:
        return 6

    return 0


total = 0
for turn in data:
    choice = choices[turn[1]]
    total += choice + compute_win(choices[turn[1]], op_choices[turn[0]])

print("Part One:", total)

total = 0

def compute_choice(you, op):
    if you == 2: # Draw
        return op + 3
    
    if you == 3: # Win
        you = op + 1
        you = 1 if you == 4 else you
        return you + 6
    
    # Loss
    you = op - 1
    you = 3 if you == 0 else you

    return you 



for turn in data:
    total += compute_choice(choices[turn[1]], op_choices[turn[0]])

print("Part Two:",total)