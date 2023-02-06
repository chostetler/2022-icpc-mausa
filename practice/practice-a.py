import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

ints = [int(s) for s in lines[0].split(' ')]
print(sum(ints))