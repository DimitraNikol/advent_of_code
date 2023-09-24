with open('input.txt', 'r') as d:
    lines = d.readlines()


def count_increased(lines):
    increased = 0

    for i in range(1,len(lines)):
        if int(lines[i-1]) < int(lines[i]):
            increased += 1
    return increased



def sums_of_three(lines):
    sumo_list = []
    for i in range(0,len(lines) -2):
        sumo_three = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        sumo_list.append(sumo_three)
    return sumo_list

print(count_increased(sums_of_three(lines)))













        

