import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

points = []
for line in lines[1:]:
    numbers = [float(s) for s in line.split(' ')]
    points.append((numbers[0], numbers[1]))

minwidth = 999999999999
for i in range(len(points)):
    point1 = points[i]
    point2 = ()
    if i==len(points)-1:
        point2 = points[0]
    else:
        point2 = points[i+1]
    
    maximumforface = 0
    for point3 in points:
        if point3==point1 or point3==point2: continue
        a = tuple(p-q for p, q in zip(point3, point1))
        b = tuple(p-q for p, q in zip(point2, point1))
        a_mag = (a[0]**2 + a[1]**2)**(1/2)
        b_mag = (b[0]**2 + b[1]**2)**(1/2)
        shadow = sum(p*q for p,q in zip(a,b)) / b_mag
        height = (a_mag**2 - shadow**2)**0.5

        # print(point1, point2, point3)
        # print(a, a_mag, b, b_mag, shadow, height)
        maximumforface = max(maximumforface, height)
    minwidth = min(maximumforface, minwidth)
print(minwidth)