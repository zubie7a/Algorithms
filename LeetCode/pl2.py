# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(set(nums)) == len(nums))

# Easy solution, can do it too with HashTable.
# Insert elements in a HashTable, if it already exists return true,
# if nothing was returned at the end return false.
