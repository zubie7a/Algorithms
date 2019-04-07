# 01 - Foregone Solution

# Key 4 is broken, we can't write a check using that digit.
# Simply split into two checks, in which one will be the original
# check but with 4s replaced with 2s, and the second check will be
# 2s in the same positions and 0s in all other positions. Or could
# do 1s and 3s! It doesn't matter! No need to make complex methods.

num_cases = int(input())
for t in range(1, num_cases + 1):
    number = input()[::-1]
    n1, n2 = "", ""
    for digit in number:
        # If the digit was a 4, but 2 in both checks at same position.
        if digit == "4":
            n1 = "2" + n1
            n2 = "2" + n2
        # If not 4, put the original digit in a check and 0 in the other.
        else:
            n1 = "0" + n1
            n2 = digit + n2

    # Case #1: 2 2
    # Case #2: 852 88
    # Case #3: 667 3777
    print("Case #{}: {} {}".format(t, int(n1), int(n2)))
