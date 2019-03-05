# https://app.codesignal.com/arcade/code-arcade/mirror-lake/BLbGNY3kEcvKjBCFC
def numberOfClans(divisors, k):
    # A set of "hashes" of states found of numbers that determine the clan.
    # The hash will be a string "0,1,1,0..." depending on whether a number
    # is divided or not by the divisors in that same position. Numbers that
    # are divided or not by divisors in the exact same positions are friends
    # and are part of a same clan. So unique hashes is the number of clans.
    clans = set([])
    # For each value in the given range...
    for i in range(1, k + 1):
        # Store whether a number divides it or not.
        divides = [i % n == 0 for n in divisors]
        # Create a string with this to "hash" the state of what divides or not.
        state = ",".join(map(str, divides))
        clans.add(state)

    return len(clans)
