# https://www.hackerrank.com/challenges/two-characters
n, s = int(raw_input()), raw_input()
# Reduce s to unique occurrences.
uniques = set(s)
maxLen = 0
# Iterate over the unique occurrences to form pairs.
for i in uniques:
    for j in uniques:
        # Pairs must be distinct.
        if i == j:
            continue
        # Filter all characters from s except for the
        # given pair.
        t = filter(lambda c: c == i or c == j, s)
        # If the resulting string has at least 2
        # characters
        if len(t) > 1:
            # c1 will be the first character, c2 the
            # second one.
            c1, c2 = t[0], t[1]
            # List that will hold True values for 
            # characters in even 0-index positions equal
            # to the first character.
            count1 = [(t[k] == c1)*(not(k % 2)) for k in range(len(t))]
            # List that will hold True values for
            # characters in odd 0-index positions equal
            # to the second character.
            count2 = [(t[k] == c2)*(k % 2) for k in range(len(t))]
            # The sum of True values from both lists
            # must be equal to the length of the 
            # filtered string.
            if sum(count1) + sum(count2) == len(t):
                # If so, keep track of the biggest 
                # filtered string.
                maxLen = max(maxLen, len(t))
print maxLen
