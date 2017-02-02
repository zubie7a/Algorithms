# Python:

from __future__ import print_function
# print(args..., sep="", end="")
from __future__ import division
# / float div, // int div

# If statements
n = int(raw_input().strip())
if n % 2 == 1:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Formatting a string:
print("%d\n%d\n%d\n" % (a + b, a - b, a * b))

# Simple loop
for i in range(3):
    print i**2

# Simple function
def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        leap = True
    return leap

# Simple lambda: print numbers from 1 to N. 12345...N
n = int(raw_input())
map(lambda x: print(x, end=""), range(1, n + 1))

# Lists
res = []
pos = 1
val = "a"
res.insert(pos, val)
res.append(val)
res.remove(val)
res.pop()
# Takes a cmp function, or a key function, or a reverse flag.
res.sort()    # or sorted(iterable)
res.reverse() # or reversed(sequence)

# Tuples
n = int(raw_input())
vals = map(lambda x: int(x), raw_input().split(" "))
# tuple(iterable)
t = tuple(vals)

# List comprehensions
# Whole list will be created on memory. Use a generator or xrange if what you want is pass a really
# long iterable to a function that will consume iterable one by one.
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
s = int(raw_input())
res = [[v1, v2, v3] for v1 in range(x+1) for v2 in range(y+1) for v3 in range(z+1) if v1+v2+v3 != s]
print(res)

# All: all in iterable are true, Any: any in iterable is true. j[::-1] trick to reverse string.
# ALL numbers are positive, any number is palindromic.
n, nums = int(raw_input()), raw_input().split(" ")
print all([int(i) >= 0 for i in nums]) and any([j == j[::-1] for j in nums])


# *: unpack iterable.
# key: the key to use to compare, useful for creating sort/priority objects, or retrieving only sorting relevant key.
# In this case, it creates a tuple where it gives relevance, such that:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Sorting1234 -> ginortS1324
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

# Make string elements accesible and convert back to string:
s = ""
x = list(s)
s = "".join(x)
# Change case of string, and validate what it is
x.swapcase()
x.isdigit()
x.issuper()
x.islower()

# Using a set for average of unique elements
num, heights = raw_input(), set([float(i) for i in raw_input().split(" ")])
print sum(heights)/len(heights)

# Operations in sets 
nA = raw_input()
sA = set([int(x) for x in raw_input().split(" ")])
instructions = int(raw_input())
for i in range(instructions):
    inst, lenSet = raw_input().split(" ")
    newSet = set(map(int, raw_input().split(" ")))
    if inst == "intersection_update":
        sA &= newSet
    elif inst == "union_update":
        sA |= newSet
    elif inst == "difference_update":
        sA -= newSet
    elif inst == "symmetric_difference_update":
        sA ^= newSet
print sum(sA)

# Check subset, >, >=, etc apply.
for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.  
    a = int(raw_input()); A = set(raw_input().split())
    b = int(raw_input()); B = set(raw_input().split())
    print A <= B

# Check if element in set
n, m = raw_input().split(" ")
nums = raw_input().split(" ")
A = set(raw_input().split(" "))
B = set(raw_input().split(" "))
print sum([(i in A) - (i in B) for i in nums])

# Pow and Pow mod
print pow(a,b)
print pow(a,b,c)

# divmod
from __future__ import division, print_function
n, m = int(raw_input()), int(raw_input())
d, m = divmod(n, m)
print (d, m, (d,m), sep="\n")

# Itertools product
# N list of values, pick one value from each list such that sum of values squared mod M is max. 
# For this, generate all possible combinations of values, using cartesian product.
from __future__ import print_function
from itertools import product

K, M = map(int, raw_input().split())
vals = [map(lambda z: int(z)**2, raw_input().split()[1:]) for _ in range(K)]
print(max(map(lambda z: sum(z)%M, product(*vals))))


# Itertools permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import permutations

v, n = raw_input().split(" ")
n = int(n)

[print(("%s"*n) % z) for z in sorted(permutations(v, n))]

# Itertools combinations
from itertools import combinations
# Read number of values, the values, and k
_, vals, k = raw_input(), raw_input().split(" "), int(raw_input())
# The combinations are all possible picks of k distinct elements, 
# regardless of order so use combination instead of permutation.
# Make it a list so its iterable (?)
combs = list(combinations(vals, k))
# For all generated tuples, check if "a" is them, and sum the True
# values, then divide by total number of possible tuples/combinations.
print sum(["a" in c for c in combs])/float(len(combs))

# Itertools combinations with replacement
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import combinations_with_replacement
v, n = raw_input().split(" ")
v, n = sorted(v), int(n)
[print("".join(z)) for z in combinations_with_replacement(v, n)]

# Itertools group by 
# Groups adjacent repeated values into single occurrence, with counter of original occurrences
from __future__ import print_function
from itertools import groupby
print(*[(len(list(y)), int(x)) for (x, y) in groupby(raw_input())])

# Counter: a generalized counter of occurences in iterable:

x = int(raw_input())
sizes = Counter(map(int, raw_input().split()))
earned = 0
customers = int(raw_input())
for i in range(customers):
    size, price = map(int, raw_input().split())
    if sizes[size] != 0:
        sizes[size] -= 1
        earned += price

print earned

# Defaultdict: a dictionary with default values
# If value doesn't exist, it will just return a default value [], 0, False, ""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from collections import defaultdict

n, m = map(int, raw_input().split())
groupA = [raw_input() for _ in range(n)]
groupB = [raw_input() for _ in range(m)]

d = defaultdict(list)
# For all values in groupA, store the place where they occur, if its
# a repeated value, then the place will be appended as multiple.
[d[groupA[i]].append(i + 1) for i in range(n)]

# For all values in groupB, print the list places they occur in groupA,
# or else if they do not occur, print -1
lists = [d[groupB[i]] for i in range(m)]
print(*map(lambda z: " ".join(map(str,z)) if len(z) > 0 else "-1", lists), sep="\n")


# NamedTuple:
from collections import namedtuple
rowNum, Row = int(raw_input()), namedtuple("Row", " ".join(raw_input().split()))
rows = [Row(*raw_input().split()) for _ in range(rowNum)]
print sum(map(lambda z: int(z.MARKS), rows)) / float(rowNum)
'''
ID         MARKS      NAME       CLASS        namedtuple receives: "ID MARKS NAME CLASS"  
1          97         Raymond    7         
2          50         Steven     4            newly created instances will receive that same amount
3          91         Adrian     9            of arguments UNPACKED, and will be accessible using
4          72         Stewart    5            the names, assigned in that same order.
5          80         Peter      6   
'''

# OrdDict: keeps track of original order
# If a entry is repeated, original position is left unchanged.
from __future__ import print_function
from collections import OrderedDict
num = int(raw_input())
odict = OrderedDict()
for i in range(num):
    word = raw_input().strip()
    if odict.get(word):
        odict[word] += 1
    else:
        odict[word] = 1

print(len(odict.keys()))
print(" ".join(map(str, odict.values())))
'''
4
bcdef     x 2
abcdefg   x 1
bcde      x 1
bcdef     x 2 (already there)
Sample Output

Print the number of unique words, and then the count in order of occurrence
3
2 1 1
'''

# Double ended queue.
from __future__ import print_function
from collections import deque
num = int(raw_input())
d = deque()
for i in range(num):
    cmd = raw_input().split()
    if cmd[0] == "append":
        d.append(cmd[1])
    elif cmd[0] == "appendleft":
        d.appendleft(cmd[1])
    elif cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()
print(*d)


from collections import deque

def array_left_rotation(a, n, k):
    d = deque(a)
    d.rotate(-k)
    a = list(d)
    return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

# Rotate list manually:



def array_left_rotation(a, n, k):
    return [a[(k + i) % n] for i in range(n)]

def array_left_rotation(a, n, k):
    return [a[(n + k + i) % n] for i in range(n)]

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

# OR... 

n, k = map(int, raw_input().split())
nums = map(int, raw_input().split())
def rot(n, k, nums):
    arr = nums[:]
    k = k % n
    for i in range(n):
        arr[(n - k + i) % n] = nums[i]
    return arr

print " ".join(map(str, rot(n, k, nums)))


# Check if a tree is a binary search tree.
def check_binary_search_tree_(root):
    resList = []
    inOrder(root, resList)
    for i in range(1, len(resList)):
        cur = resList[i]
        prev = resList[i - 1]
        if prev >= cur:
            return False
    return True

def inOrder(root, res): 
    if root is None:
        return []
    inOrder(root.left, res)
    res.append(root.data)
    inOrder(root.right, res)
    return res


"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None or head.next is None:
        return False
    n1 = head
    n2 = head.next
    while True:
        if n1 is None or n2 is None:
            return False
        if n1 == n2:
            return True
        n1 = n1.next
        n2 = n2.next
        if n2 is None:
            return False
        n2 = n2.next



# Check if the expression is matched:
# {[()]}        YES
# {[(])}        NO
# {{[[(())]]}}  YES
# {}[]()        YES
# {[]([])}      YES
# {{{{{{{{}     NO
# }}}}}}}}}     NO
# ()            YES
# )(            NO

def is_matched(expression):
    stack = []
    # Determine which closing symbol closes which opening one.
    pairs = {
        "}" : "{",
        "]" : "[",
        ")" : "(",
    }
    for i in list(expression):
        # If its an opening symbol, put it into stack.
        if any([i == x for x in pairs.values()]):
            stack.append(i)
        # If its a closing symbol, it must close the current symbol on
        # the top of the stack.
        elif any([i == x for x in pairs.keys()]):
            try:
                # If there was something to pop and it ain't the expected
                # symbol, return False.
                if pairs[i] != stack.pop():
                    return False
            except:
                # If there was nothing to pop, return False.
                return False
    # Check if the length is 0, because there could be a lot of unclosed
    # symbols still in the stack.
    return len(stack) == 0
            
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"



# Running median, that is, keep outputting the current median whilst the list
# is being built. Keep two heaps for the two halves of the list, and keep printing
# either just the top value of the left maxheap, or the average between the top at
# left maxheap, and top at right minheap


import sys
import heapq

n = int(raw_input().strip())
a_i = 0
maxh = [] # Left
minh = [] # Right
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    if len(maxh) == 0:
        heapq.heappush(maxh, -a_t)
    else:
        if len(maxh) > len(minh):
            maxtop = -(heapq.heappop(maxh))
            if maxtop > a_t:
                heapq.heappush(maxh, -a_t)
                heapq.heappush(minh, maxtop)
            else:
                heapq.heappush(maxh, -maxtop)
                heapq.heappush(minh, a_t)
        else:
            mintop = heapq.heappop(minh)
            if mintop < a_t:
                heapq.heappush(maxh, -mintop)
                heapq.heappush(minh, a_t)
            else:
                heapq.heappush(maxh, -a_t)
                heapq.heappush(minh, mintop)
    len1, len2 = len(maxh), len(minh)
    left, right = -1, -1
    if len1:
        left = -heapq.heappop(maxh)
    if len2:
        right = heapq.heappop(minh)
    if len1 == len2:
        print "%.1f" % ((left + right) / 2.0)
    else:
        print "%.1f" % float(left)
    if left != -1:
        heapq.heappush(maxh, -left)
    if right != -1:
        heapq.heappush(minh, right)




# Implement a Queue using two stacks.
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        self.pour()
        if len(self.second) > 0:
            return self.second[-1]
        
    def pop(self):
        self.pour()
        if len(self.second) > 0:
            self.second.pop()
        
    def put(self, value):
        self.first.append(value)
        
    def pour(self):
        if len(self.second) == 0:
            while len(self.first) > 0:
                self.second.append(self.first.pop())

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
# Min and Max heap for running median.
# Two stacks pouring for a queue.


    
