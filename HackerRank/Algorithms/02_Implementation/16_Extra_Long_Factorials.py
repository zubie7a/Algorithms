# https://www.hackerrank.com/challenges/extra-long-factorials
n = int(raw_input())
res = 1
# Factorial in Python, easy because big integers :-P
for i in range(1,n+1):
    res *= i
print res
