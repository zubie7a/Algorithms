# 026 - Remove Duplicates From Sorted Array (Easy)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Deduplicate elements in a sorted list, in place. This is done by
        # copying values to earlier in the list, the remainder at the end won't
        # matter because we'll return the index at which the array should "end".

        # An index to keep track of the last moved unique number.
        unique_idx = 0
        last_uniq_number = -2<<31
        for idx in range(len(nums)):
            number = nums[idx]
            # If we stopped going over duplicated numbers...
            if number != last_uniq_number:
                # Copy the current number to the latest unique position...
                nums[unique_idx] = number
                # And update the last unique number.
                last_uniq_number = number
                unique_idx += 1

        return unique_idx
