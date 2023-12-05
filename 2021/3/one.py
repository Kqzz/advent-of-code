base_input = [line.strip() for line in open("example.txt").readlines()]

line_bits = {}

for (line_num, line) in enumerate(base_input):
    for (i, char) in enumerate(line):
        line_bits[line_num] = line_bits.get(line_num, "") + char

def most_common(bits, least_common = False):
    zeroes, ones = 0, 0
    for bit in bits:
        if bit == "0":
            zeroes += 1

        if bit == "1":
            ones += 1

    if not least_common:
        return "1" if ones > zeroes else "0"
    else:
        return "1" if zeroes > ones else "0"

gamma_rate = "".join([most_common(bits) for bits in line_bits.values()][0:5])
print(gamma_rate)

print(line_bits)


# im lost
