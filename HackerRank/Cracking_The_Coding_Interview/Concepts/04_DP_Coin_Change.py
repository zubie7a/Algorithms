# https://www.hackerrank.com/challenges/ctci-coin-change
table = {}
n, m = map(int, raw_input().split())
coins = map(int, raw_input().split())
 
# index: current coin being evaluated. It will only try that coin
# once, and it will try with many multiples of that coin until
# fitting the remaining amount.
# n: the remaining amount.
def compute(index, n):
    # It added up, so this is a valid combination.
    if n == 0:
        return 1
    # It exceeded the amount, so its not a valid combination.
    if n < 0:
        return 0
    # The index exceeded capacity, so it reached the end and
    # there was still money missing.
    if index >= len(coins):
        return 0
    # If result hasn't been computed before.
    # The key to the previously computed result will be the
    # same arguments of the function used to compute it!
    if not table.get((index, n)):
        table[(index, n)] = 0
        # For all unused coins
        coin, k = coins[index], 0
        # Add multiples of coin until reaching n. 
        while k*coin <= n:            
            table[(index, n)] += compute(index + 1, n - k*coin)
            k += 1
    return table[(index, n)]
 
print compute(0, n)
