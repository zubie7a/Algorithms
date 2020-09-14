# 198 - House Robber (Easy)
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        # From a list of houses, rob houses that are not adjacent.
        # It's not enough with just robbing the odd houses or the even
        # houses, there may be a case where in 4 houses it's better to
        # rob the first and last one, but none of the in-between.

        # Store the result of being at a given house and deciding whether
        # to rob it or not how it impacts the long term result.
        cache = {}

        # Recursively at each position branch deciding whether to rob it
        # or not, unless you robbed the previous house which means can't
        # branch at current position.
        def recursively_rob(house_idx : int, nums : List[int]) -> int:

            # If we had already found this house previously...
            if cache.get(house_idx):
                return cache.get(house_idx)

            # If it's the last house, just return what if we robbed it or not.
            if house_idx + 1 == len(nums):
                last_rob = nums[house_idx]
                last_not_rob = 0
                return (last_rob, last_not_rob)

            # Get the values of the next house onwards.
            next_rob, next_not_rob = recursively_rob(house_idx + 1, nums)

            # Get the value of the money in the current house.
            curr_house_money = nums[house_idx]

            # Now, if we choose to rob the current house, we just return as rob
            # the value of the current house + the value onwards without robbing
            # the next house.
            curr_rob = curr_house_money + next_not_rob

            # Then, if we choose to not rob the current house, we return the best
            # option of robbing or not robbing the next house.
            curr_not_rob = max(next_not_rob, next_rob)

            cache[house_idx] = (curr_rob, curr_not_rob)

            return cache[house_idx]

        # This solution apparently is efficient but gets a stack overflow because
        # there's cases in Leetcode with more than 1000 length so it goes really deep.
        return max(recursively_rob(0, nums))

# This is a solution that instead of using recursion, uses the problem similar
# to fibonacci.
class Solution:
    def rob(self, nums: List[int]) -> int:

        # From a list of houses, rob houses that are not adjacent.
        # It's not enough with just robbing the odd houses or the even
        # houses, there may be a case where in 4 houses it's better to
        # rob the first and last one, but none of the in-between.

        # For no elements, the result is 0.
        if len(nums) == 0:
            return 0

        # For one element, the result is the element.
        if len(nums) == 1:
            return sum(nums)

        # For two elements, the result is the max of both elements.
        if len(nums) == 2:
            return max(nums)

        # Initialize a lookup table.
        table = [0 for _ in range(len(nums))]
        # The base cases are, for the initial house, it's own value.
        table[0] = nums[0]
        # For the second house, the max of it's value and the initial house.
        table[1] = max(nums[0], nums[1])

        # Now, for every house onwards, compute what's best, if taking the value
        # if the previous house without robbing at current, or rob at current and
        # take the value of the 2nd previous house.
        for idx in range(2, len(nums)):
            rob = table[idx - 2] + nums[idx]
            not_rob = table[idx - 1]
            table[idx] = max(rob, not_rob)

        return table[-1]

# Here's also a solution that does not use extra O(N) space but O(1):
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return sum(nums)

        if len(nums) == 2:
            return max(nums)

        maxPrev2 = nums[0]
        maxPrev1 = max(nums[0], nums[1])

        # We do not need to keep the state for every position, we just need to keep
        # track of the previous two positions visited.
        for idx in range(2, len(nums)):
            rob = maxPrev2 + nums[idx]
            not_rob = maxPrev1
            maxPrev2 = maxPrev1
            maxPrev1 = max(rob, not_rob)

        return maxPrev1
