import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

number = list(lines[0])

for row in range(3, -1, -1):
    binarydigit = 2**row
    for i in range(0, 2):
        digit = number[i]
        if int(digit)-binarydigit >= 0:
            print('* ', end='')
            number[i] = str(int(digit) - binarydigit)
        else:
            print('. ', end='')
        pass
    print('  ', end='')
    for i in range(2, 4):
        digit = number[i]
        if int(digit)-binarydigit >= 0:
            print('*', end='')
            
            number[i] = str(int(digit) - binarydigit)
        else:
            print('.', end='')
        if i == 2:
                print(' ', end='')
        pass
    print('')

