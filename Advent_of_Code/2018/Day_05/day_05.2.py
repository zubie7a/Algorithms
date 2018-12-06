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
    # Now for each polymer, remove from the beginning one unit at a
    # time (both the lower case and upper case) to see how far can
    # the polymer be reduced without this unit being present. The
    # unit preventing the lowest reduction is the faulty one.
    polymer_bak = polymer
    lowest_len = 1<<31

    for i in range(26):
        lower_char = chr(ord('a') + i)
        upper_char = lower_char.upper()
        # Remove from the original backed up polymer.
        polymer = polymer_bak.replace(lower_char, "")
        polymer = polymer.replace(upper_char, "")
        # Now do the same thing than part 1, finding the most reduced state,
        # but then keeping track of its length to find shortest most reduced.
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

        if len(polymer) < lowest_len:
            lowest_len = len(polymer)

    # Result: 5302.
    print(lowest_len)
