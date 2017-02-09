# https://www.hackerrank.com/challenges/between-two-sets
lenA, lenB = map(int, raw_input().split())
setA = map(int, raw_input().split())
setB = map(int, raw_input().split())

# The count of numbers "between" setA and setB.
# A number X is between setA and setB if all elements
# from setA divide evenly the number, and if the number
# divides evenly all elements from setB.
count = 0
maxA, minB = max(setA), min(setB)
# Iterate from the max of setA to min of setB, inclusive.
for num in range(maxA, minB + 1):
    # Check the between property.
    left = all([num % numA == 0 for numA in setA])
    right = all([numB % num == 0 for numB in setB])
    # If it fulfills both, then increase the count of
    # numbers "between" the two sets.
    count += left*right
print count
