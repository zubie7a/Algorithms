# https://www.hackerrank.com/challenges/cut-the-sticks
n = int(raw_input())
sticks = sorted(map(int, raw_input().split()))
i, cur_stick = 0, 0
# While there are remaining sticks.
while i < len(sticks):
    # The amount of sticks that will be cut are the
    # remaining ones at the start of an iteration.
    print len(sticks) - i
    # Store the current stick. 
    cur_stick = sticks[i]
    # Advance the iterator until you meet an stick
    # bigger than the current length, as all the ones
    # with the current length will have been erased at
    # this iteration.
    while cur_stick == sticks[i] and i < len(sticks):
        i += 1
