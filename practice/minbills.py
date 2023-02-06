import math

def least_bills(denoms, n):
    least_bills_dp = [math.inf for n in range(n+1)]
    least_bills_dp[0] = 0
    for rem in range(1, n+1):
        min_bills = math.inf
        for denom in [d for d in denoms if d<=rem]:
            min_bills = min(min_bills, least_bills_dp[rem-denom]+1)
        least_bills_dp[rem] = min_bills
    return least_bills_dp[n]

denominations = [2, 3, 6, 7, 8]
rarity = []
for i in range(60):
    print(i, ":", least_bills(denominations, i))