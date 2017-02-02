# https://www.hackerrank.com/challenges/py-check-subset
# More than 4 lines will result in 0 score. Blank lines won't be counted.  
for i in range(int(raw_input())): 
    a = int(raw_input()); setA = set(raw_input().split())
    b = int(raw_input()); setB = set(raw_input().split())
    print setA < setB
