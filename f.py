import sys

lines = []
for i in sys.stdin:
    lines.append(i.strip())

inputstring = lines[0]

ways_to_close_dp = {}
dict_uses = 0
def ways_to_close(i, openers):
    global dict_uses
    if str([i,openers]) in ways_to_close_dp.keys():
        dict_uses += 1
        return ways_to_close_dp[str([i, openers])]
    if len(openers) > len(inputstring)-i+1:
        ways_to_close_dp[str([i, openers])] = 0
        return 0
    if len(openers)==len(inputstring)-i+1:
        ways_to_close_dp[str([i, openers])] = 1
        return 1
    if i == len(inputstring):
        if openers == '':
            ways_to_close_dp[str([i, openers])] = 1
            return 1
        else:
            ways_to_close_dp[str([i, openers])] = 0
            return 0
    x = inputstring[i]
    if x == '?':
        sum = 0
        if len(openers) > 0:
            sum += ways_to_close(i+1, openers[0:-1])
        for bracket in '{<([':
            sum += ways_to_close(i+1, openers+bracket)
        ways_to_close_dp[str([i, openers])] = sum
        return sum
    elif x in '{<([':
        to_be_returned = ways_to_close(i+1, openers + x)
        ways_to_close_dp[str([i, openers])] = to_be_returned
        return to_be_returned
    elif x in '}>)]':
        # print('openers:', openers)
        if len(openers)>0 and ((x=='}' and openers[-1]=='{') or (x=='>' and openers[-1]=='<') or (x==']' and openers[-1]=='[') or (x==')' and openers[-1]=='(')):
            to_be_returned = ways_to_close(i+1, openers[:-1])
            ways_to_close_dp[str([i, openers])] = to_be_returned
            return to_be_returned
        else:
            ways_to_close_dp[str([i, openers])] = 0
            return 0
    
print(ways_to_close(0, ''))
# print(ways_to_close_dp)