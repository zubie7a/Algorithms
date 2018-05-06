# https://www.hackerrank.com/challenges/richie-rich
n, k = map(int, raw_input().split())
# A list of tuples, with the value of each place,
# and a boolean to mark whether this place has been
# changed previously or not.
nums = [(int(i), False) for i in list(raw_input())]
# First have try palindrome by changing one by one,
# making pairs match according to highest value in pair.
for i in range(0, n/2):
    # For each pair on the extremes, change the
    # value of the lower one to the one of the
    # bigger one, this consumes only one k.
    numA, numB = nums[i], nums[-i-1]
    if numA[0] > numB[0] and k > 0:
        numB = (numA[0], True)
        k -= 1
    if numB[0] > numA[0] and k > 0:
        numA = (numB[0], True)
        k -= 1
    nums[i], nums[-i-1] = numA, numB

# Now with the remaining k, convert pairs to 9's.
for i in range(0, n/2):
    numA, numB = nums[i], nums[-i-1]
    # Just do stuff if pairs aren't already 9.
    if numA[0] != 9 and numB[0] != 9:
        # Both True: both changed before
        # Both False: neither changed before
        if numA[1] == numB[1] and k > 1:
            # Will cost 2 only if both were intact.
            k -= 2*(not numA[1])
            # If both were already changed, changing
            # to 9 will be free because its as if they
            # were changed to 9 originally.
            numA, numB = (9, True), (9, True)
        # True and False: just one changed before
        elif numA[1] != numB[1] and k > 0:
            # It will just cost one, because one was
            # changed and the other wasn't, so the
            # one that was changed to match the second
            # one, its now as if it was changed to
            # 9 originally and the second one now too.
            k -= 1
            numA, numB = (9, True), (9, True)
    nums[i], nums[-i-1] = numA, numB

# Now, if the string has an odd length, try putting
# the middle value as 9 if you still can.
if n % 2 == 1 and k > 0:
    nums[n/2] = (9, True)
    k -= 1

res = "".join(map(lambda x: str(x[0]), nums))
if res == res[::-1]:
    print res
else:
    print -1
