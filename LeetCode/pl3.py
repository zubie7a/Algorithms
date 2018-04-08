# https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if dic.get(num) is not None:
                if i - dic[num] <= k:
                    return True
                else:
                    dic[num] = i
            else:
                dic[num] = i
        return False
                
# Check if there's duplicate elements within k proximity in array.
# In a hash table store the last known index for a given value,
# if the value is found again, check if last known index is within k
# of current index. If not, then update the new known index.
