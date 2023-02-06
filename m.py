import sys
from collections import deque

lines = []
for i in sys.stdin:
    lines.append(i.strip())

# packets are listed in t_i order
packets = [[int(s) for s in line.split(' ')] for line in lines[1:]]

# sort packets by i
# O(nlogn)
input_ordered = deque(sorted(packets, key=lambda packet: packet[1]))

optimal_time = input_ordered[-1][1]

stream_time = 1
while len(input_ordered) >= 1:
    next_packet = input_ordered[0]
    intended_time = next_packet[1]
    arrival_time = next_packet[0]
    stream_time = max(stream_time, arrival_time)

    # print('packet', intended_time, 'playing at', stream_time)
    stream_time += 1

    input_ordered.popleft()

lag = stream_time - optimal_time - 1
print(lag)