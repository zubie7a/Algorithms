# 412 - Fizz Buzz (Easy)
# https://leetcode.com/problems/fizz-buzz/

# Classical FizzBuzz :-)
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [(i%3==0)*"Fizz"
              + (i%5==0)*"Buzz" 
              + (str(i) if i%3!=0 and i%5!=0 else "") 
                for i in range(1, n + 1)]