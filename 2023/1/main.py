import string
import re

lines = [line.strip() for line in open('input.txt')]

c = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

total = 0

for line in lines:
    occorrunces = {}
    for word in c.keys():
        for x in re.finditer(word, line):
            occorrunces[x.start()] = c[word]
    for char in string.digits:
        for x in re.finditer(char, line):
            occorrunces[x.start()] = int(char)

    occorrunces = dict(sorted(occorrunces.items()))
    print(occorrunces)
    
    digits = [k for k in occorrunces.values()]
    print(digits)
    for i, d in enumerate(digits):
        if d in c.keys():
              digits[i] = c[d]
    thingy = int(str(digits[0]) + str(digits[-1]))
    print(line, digits)
    total += thingy

print(total) 
