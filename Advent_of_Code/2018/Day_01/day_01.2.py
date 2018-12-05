# https://adventofcode.com/2018/day/1

frequencies = []

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = int(input())
        # print(line)
        frequencies.append(line)
except Exception:
    # print("EOF")
    None

# Frequency, will be changed by each command/adjustment read in a line. 
freq = 0
# Already seen states of frequencies, to know when we visit a know freq.
seen = {}
# Initialize 0 as seen because it's the initial frequency.
seen[0] = 1
# To keep track that a repeated frequency was found.
found = False

# Super inefficient because has to repeat several times whole cycle
# until finding a repeated sequence.
while not found:
    for freq_line in frequencies:
        freq += freq_line
        if freq in seen.keys():
            found = True
            break
        else:
            seen[freq] = 1

# Result: 75108.
print("Freq {} was found twice first.".format(freq))
