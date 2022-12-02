lines = [l.strip() for l in open("input.txt", "r", encoding="UTF-8").readlines()]

parts = [[]]

for line in lines:

    if line == "":
        parts.append([])
        continue

    parts[-1].append(int(line))

maximum = 0

for section in parts:
    if sum(section) > maximum:
        maximum = sum(section)

print("Stage One Max:", maximum)

parts.sort(key=sum, reverse=True)
ints = [sum(part) for part in parts[0:3]]
print(sum(ints))