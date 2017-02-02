# https://www.hackerrank.com/challenges/nested-list

arr = []
lws, snd = 1<<31, 1<<31
# Print the names of students with second lowest scores.
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    arr.append([score, name])
    if score < lws:
        snd = lws
        lws = score
    if score > lws and score < snd:
        snd = score
arr.sort()

for i in range(len(arr)):
    if arr[i][0] == snd:
        print arr[i][1]
