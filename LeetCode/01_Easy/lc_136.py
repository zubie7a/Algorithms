# 136 - Single Number (Easy)
# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums))*2 - sum(nums)) 
        
# (sum(set(nums))* k - sum(nums)) / (k - 1)
# When there's values that happens k times in a list, except for
# a value that happens only once. Get a ideal sum (all values
# happen k times) by getting a set, getting its sum and multiplying
# by k, and then substract the sum of the actual list. All values
# That really happened k times will be cancelled, but the one that
# happened only once, will leave a remainder of value * (k - 1), so
# divide by (k - 1) to get the actual value.

# Can also be done by XORing several times, the XOR is commutative,
# and X ^ X == 0, so at some point the odd one out will be the result.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res
         
         
# Also can use reduce (interesting). The first var in lambda is the
# accumulator, the second the item retrieved from the iterable.      
    return reduce(lambda x, y: x^y, nums)
