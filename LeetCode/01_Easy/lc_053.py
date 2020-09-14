# 053 - Maximum Subarray (Easy)
# https://leetcode.com/problems/maximum-subarray/submissions/

# Use Kadane's Algorithm!
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Find the max subarray ending at each index.
        # The max subarray ending at 0th index is just the value.

        # What if array is empty?
        # Apparently Leetcode judge isn't checking this case, the manual tester
        # tells me that for input [] the result should be "-2147483648" but I
        # return 0.
        if len(nums) == 0:
            return 0

        # Now start computing...
        max_local_subarrays = []
        for idx in range(len(nums)):
            value = nums[idx]
            # The max subarray ending at current position will be either
            # just the current value, or the current value + previous max
            # local subarray.
            if idx == 0:
                max_local_subarrays.append(value)
            else:
                max_local_subarrays.append(max(value, value + max_local_subarrays[-1]))

        return max(max_local_subarrays)

# Can also do it without extra arrays...
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Find the max subarray ending at each index.
        # The max subarray ending at 0th index is just the value.

        # What if array is empty?
        # Apparently Leetcode judge isn't checking this case, the manual tester
        # tells me that for input [] the result should be "-2147483648" but I
        # return 0.
        if len(nums) == 0:
            return 0

        # Now start computing...
        max_local_subarray_sum = nums[0]
        max_global_subarray_sum = nums[0]

        for idx in range(1, len(nums)):
            value = nums[idx]
            # The max subarray ending at current position will be either
            # just the current value, or the current value + previous max
            # local subarray.
            max_local_subarray_sum = max(max_local_subarray_sum + value, value)
            max_global_subarray_sum = max(max_local_subarray_sum, max_global_subarray_sum)

        return max_global_subarray_sum
