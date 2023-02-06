import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

parts = [float(s) for s in lines[0].split()]
print(0.5 * parts[0] * parts[1])