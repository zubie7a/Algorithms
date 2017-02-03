# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
def fibonacci(n):
    # Do fibonacci without recursion! Otherwise it will blow up
    # much before fib(20~30). Precompute values and store in
    # an array. 0 and 1 will be the seed values.
    fib = [0, 1]
    for i in xrange(1, 42):
        fib.append(fib[i] + fib[i - 1])
    return fib[n]
        
n = int(raw_input())
print(fibonacci(n))

# ... Or a solution that does use recursion but also keeping
# already found results in a table.
fibs = {}
def fibonacci(n):
    # The base cases.
    if n == 0 or n == 1:
        return n
    # If number has already been computed, return it.
    if fibs.get(n):
        return fibs[n]
    # This is a solution that uses recursion but also a table to
    # store already found results so that it prunes recursion trees.
    fibs[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibs[n]
        
n = int(raw_input())
print(fibonacci(n))
