import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

tankstart = int(lines[0].split(' ')[1])
tank = tankstart

fills = 0
for line in lines[1:]:
    size = 0
    if 'L' in line:
        size += 1
    size += int(line[0])
    if tank < size:
        tank = tankstart
        fills += 1
    tank -= size
    
print(fills)