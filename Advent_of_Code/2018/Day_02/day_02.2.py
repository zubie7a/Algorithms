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

# Assuming strings with same length, return the number of diff chars
# at same position, and the list of characters that are the same.
def cmp(str_a, str_b):
    diff = 0
    common = ""
    for i in range(len(str_a)):
        char_a = str_a[i]
        char_b = str_b[i]
        if char_a != char_b:
            diff += 1
        else:
            common += char_a

    return (diff, common)

# Compare all possible pairs of strings to find the one where there's
# only one differing character at the same possition.
res = ""
for line_1 in lines:
    for line_2 in lines:
        diff, common = cmp(line_1, line_2)
        if diff == 1:
            res = common

# Print the common characters between these two strings.
# Result: qysdtrkloagnfozuwujmhrbvx.
print(res)
