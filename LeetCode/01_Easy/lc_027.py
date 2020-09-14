# 027 - Remove Element (Easy)
# https://leetcode.com/problems/remove-element/submissions/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # Remove a certain value in a list, in-place.
        # Do this by moving to the left all found instances
        # of different values, and returning an index at which
        # the array should "end".
        res_idx = 0
        for idx in range(len(nums)):
            num = nums[idx]
            if num != val:
                nums[res_idx] = num
                res_idx += 1
        
        return res_idx
