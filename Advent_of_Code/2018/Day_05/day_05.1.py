# https://adventofcode.com/2018/day/5

# List of logs to read from STDIN.
polymers = []

# test_polymers = [
#     "dabAcCaCBAcCcaDA"
# ]

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = str(input())
        # print(line)
        polymers.append(line)
except Exception:
    # print("EOF")
    None

reactive_pairs = []
# Generate possible pairs to substitute, e.g. "aA", "Aa" ... "zZ", "Zz".
for i in range(26):
    char = chr(ord('a') + i)
    reactive_pairs.append(char + char.upper())
    reactive_pairs.append(char.upper() + char)

for polymer in polymers:

    changed = True
    while changed:
        changed = False
        previous_length = len(polymer)
        for pair in reactive_pairs:
            # Replace this pair everywhere in string by empty character.
            polymer = polymer.replace(pair, "")
            # If the length was changed, keep reacting, until no changes
            # were made meaning the most reduced state has been reached.
            if previous_length != len(polymer):
                changed = True

    # Result: 11636.
    print(len(polymer))


# INITIAL EXTREMELY INEFFICIENT SOLUTION.

# def opposite_case(char_a, char_b):
#     # Both characters have to be alphabetic.
#     if (not char_a.isalpha()) or (not char_b.isalpha()):
#         return 0
#     # One has to be upper case and one has to be lowercase.
#     if char_a.islower() == char_b.islower():
#         return 0

#     return char_a.lower() == char_b.lower()

# for polymer in polymers:
#     while True:
#         changed = False
#         for i in range(len(polymer) - 1):
#             pre = polymer[i]
#             pos = polymer[i + 1]
#             # Check pairs of consecutive characters, if they are same
#             # but opposite case remove them and reset the string from
#             # the start, very inefficient.
#             if opposite_case(pre, pos):
#                 polymer = polymer[:i] + polymer[i + 2:]
#                 changed = True
#                 break
#         if not changed:
#             break
#     print(polymer)