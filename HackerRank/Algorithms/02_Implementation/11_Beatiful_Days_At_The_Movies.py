# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
i, j, k = map(int, raw_input().split())
days = 0
# A day between i and j is beautiful if the absolute difference
# of the number and its reverse is evenly divisible by k.
for number in range(i, j + 1):
    reverse = int(str(number)[::-1])
    days += (abs(number - reverse) % k) == 0
print days
