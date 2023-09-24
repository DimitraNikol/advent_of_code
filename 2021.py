with open('input.txt', 'r') as d:
    lines = d.readlines()

def count_increased(lines):
    increased = 0

    for i in range(1,len(lines)):
        if int(lines[i-1]) < int(lines[i]):
            increased += 1
    return increased

print(count_increased(lines))









        

