data = [line.strip() for line in open("input.txt").readlines()]

def val(l):
    if l == "": return 0
    x = ord(l) - 96
    if x <= 0:
        x = ord(l) - 38
    return x

sums = 0
for x in data:
    s, e = x[:int(len(x)/2)], x[int(len(x)/2):]
    common = ""
    for l in s:
        if e.find(l) > -1:
            common = l
    
    sums += val(common)

print(sums)

data = list(zip(*[iter(data)] * 3))
sums = 0

for g in data:
    common = ""
    for l in g[0]:
        if g[1].count(l) > 0 and g[2].count(l) > 0:
            common = l
    
    sums += val(common)

print(sums)
