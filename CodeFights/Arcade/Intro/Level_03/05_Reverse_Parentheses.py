# https://codefights.com/arcade/intro/level-3/3o6QFqgYSontKsyk4
def reverseParentheses(s):
    # In: "a(bc)de"
    # Out: acbde
    # 
    # In: "a(bcdefghijkl(mno)p)q"
    # Out: "apmnolkjihgfedcbq"
    #
    stack = []
    orientation = -1
    s = "(" + s + ")"
    for i in range(len(s)):
        # If parentheses start, create a new stack level.
        if s[i] == "(":
            orientation = -orientation
            stack.append("")
            continue
        # If parentheses end, remove last stack level
        # and add it to the result.
        if s[i] == ")":
            orientation = -orientation
            if len(stack):
                oldTop = ""
                top = stack.pop()
                # Add the current level to the previous level
                # (if any) using the previous level orientation.
                if len(stack):
                    oldTop = stack.pop()
                if orientation == 1:
                    oldTop += top
                else:
                    oldTop = top + oldTop
                stack.append(oldTop)
            continue
        top = ""
        # Add the current character to the top word at the stack,
        # while using orientation to determine how to accumulate it.
        if len(stack):
            top = stack.pop()
        if orientation == 1:
            top += s[i]
        else:
            top = s[i] + top
        stack.append(top)
    # The result will be the last element at the top of the stack.
    return stack.pop()
