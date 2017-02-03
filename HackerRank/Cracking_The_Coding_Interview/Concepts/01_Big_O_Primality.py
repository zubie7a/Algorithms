# https://www.hackerrank.com/challenges/ctci-big-o
t = int(raw_input())
for _ in xrange(t):
    num = int(raw_input())
    i = 2
    prime = True
    # This takes O(sqrt(n)) operations.
    while i*i <= num:
        # A prime is divided only by 1 or itself.
        # Since this starts at 2 and stops at sqrt(n),
        # if it can be divided by any number along the
        # way then it is not a prime.
        if num % i == 0:
            prime = False
        i += 1
    # Special case is 1, it is not prime.
    if num == 1:
        prime = False

    print "Prime"*(prime) + "Not prime"*(not prime)
