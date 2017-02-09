# https://www.hackerrank.com/challenges/plus-minus
n = float(raw_input())
# For a list of numbers, print the relative proportion
# of positive, negative, and zeros on the list.
nums = map(int, raw_input().split())
pos, neg, zer = 0,0,0
for num in nums:
    pos += num > 0
    neg += num < 0
    zer += num == 0
print "%f\n%f\n%f" % (pos/n, neg/n, zer/n)
