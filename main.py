with open("input.txt", 'r') as f:
    lines = f.readlines()


def calories_per_elf(lines):
    elves = []
    sum = 0

    for line in lines:
        line = line.strip()

        if line == '':
            elves.append(sum)
            sum = 0
            continue

        sum += int(line)

    elves.append(sum)
    return elves

elves = calories_per_elf(lines)

max_elves = max(elves)

print(sum(list(reversed(sorted(elves)))[:3]))


