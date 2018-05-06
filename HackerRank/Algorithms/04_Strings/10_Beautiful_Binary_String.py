# https://www.hackerrank.com/challenges/beautiful-binary-string
n, binstr = int(raw_input()), raw_input()
i, changes = 0, 0
while i < len(binstr):
    non, cur = "010", binstr[i:i+3]
    if non == cur:
        # Whenever a 010 is found, changing the last
        # character to 1 so to make 011, will ruin
        # any possible 010 that started with the 
        # previous last 0, thus minimizing the amount
        # of changes required to be done.
        binstr = binstr[:i+2] + "1" + binstr[i+3:] 
        changes += 1
    i += 1
print changes
