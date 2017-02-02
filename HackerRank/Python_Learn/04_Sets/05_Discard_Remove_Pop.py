# https://www.hackerrank.com/challenges/py-set-discard-remove-pop
n = int(raw_input())
setZ = set(map(int, raw_input().split()))
m = int(raw_input())
for i in range(m):
    line = raw_input().split()
    if line[0] == "pop":
        setZ.pop()
    elif line[0] == "remove":
        setZ.remove(int(line[1]))    
    elif line[0] == "discard":
        setZ.discard(int(line[1]))
print sum(setZ)
