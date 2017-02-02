# https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    stack = []
    symbols = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    for c in expression:
        # If its an opening symbol, put it in the stack.
        if c == "{" or c == "(" or c == "[":
            stack.append(c)
        # If its a closing symbol
        else:
            # If there's something in the stack and it matches the symbol...
            if len(stack) > 0 and symbols[c] == stack[-1]:
                # Remove the symbol on top of the stack.
                stack.pop()
            # If it was a closing symbol and there's nothing in the stack,
            # or if what was on top of the stack doesn't match it...
            else:
                # It is not balanced.
                return False
    # If after consuming the expression there's still stuff in the stack,
    # then it is not matched. e.g. expression "{{{{{((((([[[[]"
    if len(stack) > 0:
        return False
    # If the stack was empty at the end, then it is matched.
    else:
        return True
        
        
t = int(raw_input())
for i in xrange(t):
    expression = raw_input()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
