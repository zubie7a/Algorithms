# 001 - Two Sum (Easy)
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = { nums[index] : index for index in range(len(nums)) }

        for idx_1 in range(len(nums)):
            num = nums[idx_1]
            diff = target - num
            if diff in nums_dict:
                idx_2 = nums_dict[diff]
                if idx_1 != idx_2:
                    return sorted(list([idx_1, idx_2]))