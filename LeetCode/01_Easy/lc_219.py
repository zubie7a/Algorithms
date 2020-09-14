# 219 - Contains Duplicate II (Easy)
# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Find if there are duplicate values that are within each other by
        # at most k. Iterate over the list keeping track of the last known
        # position for a given value. If found again, return upon finding
        # the first case where the difference in indices is at most k.

        last_position = {}
        for idx in range(len(nums)):
            num = nums[idx]
            # Be careful, the value can be 0 and it won't enter the if.
            if (last_position.get(num) is not None) and idx - last_position[num] <= k:
                return True

            last_position[num] = idx

        return False

# Check if there's duplicate elements within k proximity in array.
# In a hash table store the last known index for a given value,
# if the value is found again, check if last known index is within k
# of current index. If not, then update the new known index.
