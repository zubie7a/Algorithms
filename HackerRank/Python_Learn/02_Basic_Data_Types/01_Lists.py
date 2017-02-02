# https://www.hackerrank.com/challenges/python-lists/submissions/code/32247585
from __future__ import print_function

n = int(raw_input())
res = []
for i in range(n):
    comm = raw_input().split(" ")
    # Insert will put value at a given position.
    if comm[0] == "insert":
        pos = int(comm[1])
        val = int(comm[2])
        res.insert(pos, val)
    # Append will put value in the end.
    elif comm[0] == "append":
        val = int(comm[1])
        res.append(val)
    # Remove will take out the first occurrence. Will give error if the
    # value is not present in the list.
    elif comm[0] == "remove":
        val = int(comm[1])
        res.remove(val)
    # Pop will take value from the tail of the list.
    elif comm[0] == "pop":
        res.pop()
    # Sort will leave the list sorted. Use "sorted" to not modify original.
    elif comm[0] == "sort":
        res.sort()
    # Reverse will reverse the list, use "reversed" to not modify original.
    elif comm[0] == "reverse":
        res.reverse()
    # Print will print the list with its nested structures.
    elif comm[0] == "print":
        print(res)
