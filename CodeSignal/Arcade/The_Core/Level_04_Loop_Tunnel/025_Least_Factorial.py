# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/7BFPq6TpsNjzgcpXy/
def leastFactorial(n):
    # What's the highest factorial number that is bigger than n?
    i, fact = (1, 1)
    # Keep increasing a cumulative factorial until n can't no longer contain
    # it. If n becomes 1, then n was a factorial, if n becomes 0, then the
    # next factorial is above n.
    while(n/fact > 1):
        fact *= i
        i += 1

    return fact
