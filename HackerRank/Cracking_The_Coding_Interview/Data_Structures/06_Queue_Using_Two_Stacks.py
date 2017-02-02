# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

# A queue object using two stacks.
class MyQueue(object):
    # Initialize by declaring to arrays/stacks.
    def __init__(self):
        self.first = []
        self.second = []
    # Whenever we want to know whats on top of the stack, pour the first
    # array into the second one (but reversed), unless there's still stuff
    # on the second stack from a previous pouring. This way, the oldest
    # elements from the first (which will be at the bottom) will be the
    # first ones when the second gets the first reversed.
    def pour(self):
        if len(self.second) == 0:
            self.second = self.first[::-1]
            self.first = []

    # Peek: return the element on top of the stack.
    def peek(self):
        self.pour()
        if len(self.second) != 0:
            return self.second[-1]

    # Pop: remove the element on top of the stack.
    def pop(self):
        self.pour()
        if len(self.second) != 0:
            self.second.pop()

    # Put: put an element on top of the stack.
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    # 1: Enqueue
    if values[0] == 1:
        queue.put(values[1])   
    # 2: Dequeue
    elif values[0] == 2:
        queue.pop()
    # 3: Peek
    else:
        print queue.peek()
