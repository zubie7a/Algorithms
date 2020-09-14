# 231 - Power Of Two (Easy)
# https://leetcode.com/problems/power-of-two/submissions/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n and (n & (n-1)) == 0
