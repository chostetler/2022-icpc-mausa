import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

alice_numbers = [int(s) for s in lines[0].split(' ')]
partitions = [list(range(1, alice_numbers[0])), list(range(alice_numbers[0]+1, alice_numbers[1])), list(range(alice_numbers[1]+1, 10))]

p = [alice_numbers[0]-1, alice_numbers[1]-alice_numbers[0]-1, 9-alice_numbers[1]]
b = [0, 0, 0]

i = 0
for char in lines[1]:
    if char=='A':
        i += 1
    if char=='B':
        b[i] += 1


# print(alice_numbers)
# print(p)
# print(b)
# print(partitions)

output = []
for i in range(3):
    if b[i] >= 1:
        if b[i] == p[i]:
            output += partitions[i]

if len(output) == 2:
    print(' '.join([str(i) for i in output]))
else:
    print(-1)

