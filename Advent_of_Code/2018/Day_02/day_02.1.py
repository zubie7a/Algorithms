# https://adventofcode.com/2018/day/2
from collections import Counter

lines = []

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = str(input())
        # print(line)
        lines.append(line)
except Exception:
    # print("EOF")
    None

# The counts of words where at least one character occurs twice, and
# where at least one character occurs thrice.
count_2, count_3 = 0, 0

# Once you find a two-times character, stop counting for this word
# since it only matters once.
for line in lines:
    counter = Counter(line)
    # print(counter)
    for key in counter.keys():
        if counter[key] == 2:
            count_2 += 1
            break

# Once you find a three-times character, stop counting for this word
# since it only matters once.
for line in lines:
    counter = Counter(line)
    # print(counter)
    for key in counter.keys():
        if counter[key] == 3:
            count_3 += 1
            break

result = count_2 * count_3

# Result: 4980.
print(result)
