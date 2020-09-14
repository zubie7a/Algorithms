# 020 - Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # A stack for symbols.
        stack = []
        for idx in range(len(s)):
            symbol = s[idx]

            # If it's an opening symbol, append it into the stack.
            if symbol in ["(", "[", "{"]:
                stack.append(symbol)
            # If it's anything else...
            else:
                # If there's nothing in the stack, definitely a bad string.
                if len(stack) == 0:
                    return False
                last_symbol = stack.pop()
                # If there's something in the stack, and the current symbol
                # is not what's expected to close that...
                cond_1 = last_symbol == "(" and symbol != ")"
                cond_2 = last_symbol == "[" and symbol != "]"
                cond_3 = last_symbol == "{" and symbol != "}"
                # ... for any of the possible pairs, then it's an invalid string.
                if any([cond_1, cond_2, cond_3]):
                    return False

        # If the string was so far "valid" but not enough symbols closed it.
        if len(stack):
            return False
        # If the string was fully consumed, or was empty to begin with.
        return True

# obj = Solution()
# print(obj.isValid("()"))
# print(obj.isValid("()[]{}"))
# print(obj.isValid("(]"))
# print(obj.isValid("([)]"))
# print(obj.isValid("{[]}"))
# print(obj.isValid("{"))
# print(obj.isValid("}"))
# print(obj.isValid(""))
