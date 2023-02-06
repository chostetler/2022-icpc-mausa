import sys, math
lines = []
for highest_prime_index in sys.stdin:
    lines.append(highest_prime_index.strip())

params = [int(s) for s in lines[0].split(' ')]

D = params[2]
day_length = params[1]

practice_lengths = [int(line) for line in lines[1:]]

day_order_dict = {}
passes_completed_dict = {}
current_student_index = 0
cycle_found = False
cycle_start = None


while not cycle_found:
    hours_remaining = day_length
    starting_student_index = current_student_index
    passes_completed = 0
    while hours_remaining >= practice_lengths[current_student_index]:
        if hours_remaining >= sum(practice_lengths):
            passes_completed += math.floor(hours_remaining/sum(practice_lengths))
            hours_remaining -= sum(practice_lengths) * math.floor(hours_remaining/sum(practice_lengths))
        else:
            hours_remaining -= practice_lengths[current_student_index]
            current_student_index = (current_student_index + 1) % len(practice_lengths)
            if current_student_index == 0:
                passes_completed += 1
    day_order_dict[starting_student_index] = current_student_index
    passes_completed_dict[starting_student_index] = passes_completed

    if current_student_index in day_order_dict.keys():
        cycle_start = current_student_index
        cycle_found = True

d1 = 0
p1 = 0
current_student_index = 0
# Figure out stuff on path to cycle
while current_student_index is not cycle_start:
    d1 += 1
    p1 += passes_completed_dict[current_student_index]
    current_student_index = day_order_dict[current_student_index]

# print('d1', d1)
# print('p1', p1)

dc = 1
pc = passes_completed_dict[cycle_start]
# Figure out stuff in cycle
current_student_index = day_order_dict[cycle_start]
days = 1
while current_student_index is not cycle_start:
    dc += 1
    pc += passes_completed_dict[current_student_index]
    current_student_index = day_order_dict[current_student_index]

# print('dc', dc)
# print('pc', pc)

full_cycles_completed = math.floor((D-d1)/dc)
P = p1 + pc * full_cycles_completed
remainder_days = D - d1 - (dc * full_cycles_completed)

current_student_index = cycle_start
while remainder_days > 0:
    P += passes_completed_dict[current_student_index]
    remainder_days -= 1
    current_student_index = day_order_dict[current_student_index]

print(P)


# print(day_order_dict)
# print(passes_compl
# eted_dict)
# print(cycle_start)