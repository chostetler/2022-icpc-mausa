import sys, math

lines = []
for i in sys.stdin:
    lines.append(i.strip())

dimensions = [int(s) for s in lines[0].split(' ')]
rows_count = dimensions[0]
cols_count = dimensions[1]

rows = [line.split(' ') for line in lines[1:]]

zeros = 0
ones = 0
twos = 0
for row in rows:
    zeros += row.count('0')
    ones += row.count('1')
    twos += row.count('2')

if zeros >= 2:
    print(0)
elif zeros == 1:
    if rows_count >= 2 and cols_count >= 2:
        if ones >= 1:
            print(1)
        else:
            print(2)
    elif rows_count == 1:
        end1 = int(rows[0][0])
        end2 = int(rows[0][-1])
        if (end1==0) or (end2==0):
            print(max([end1, end2]))
        else:
            print(min([end1, end2]))
    elif cols_count == 1:
        end1 = int(rows[0][0])
        end2 = int(rows[-1][0])
        if (end1==0) or (end2==0):
            print(max([end1, end2]))
        else:
            print(min([end1, end2]))
elif zeros == 0:
    if twos%2==0:
        print(0)
    else:
        goal_twos = math.floor(twos/2)
        print(2**goal_twos)
