data = [l.strip()
        for l in open("input.txt", "r", encoding="UTF-8").readlines()]


def parse(s):
    s = s.split(",")
    s[0] = s[0].split("-")
    s[1] = s[1].split("-")
    return s


def section(elf):
    return list(range(int(elf[0]), int((elf[1])) + 1))


def find_sub(l, l2):
    return [x in l for x in l2]


p1 = 0
p2 = 0
for s in data:
    s = parse(s)
    first = section(s[0])
    second = section(s[1])
    if all(find_sub(first, second)) or all(find_sub(second, first)):
        p1 += 1

    if any(find_sub(first, second)) or any(find_sub(second, first)):
        p2 += 1

print(p1, p2)
