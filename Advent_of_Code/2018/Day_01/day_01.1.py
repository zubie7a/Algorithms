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

for freq_line in frequencies:
    freq += freq_line

# Result: 536.
print("Freq at end of first full iteration is {}".format(freq))
