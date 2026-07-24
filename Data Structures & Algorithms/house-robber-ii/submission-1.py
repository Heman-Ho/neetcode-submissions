class Solution:
    def rob(self, nums: List[int]) -> int:
        # We split the circle into two lines: 
        # 1. the line includes house 0 and excludes house n - 1
        # 2. the line excludes house 0 and includes house n
        # This ensures we meet the circle constraint

        # Edge cases: 1 or 2 houses
        if len(nums) <= 3:
            return max(nums)

        # Helper function solves standard House Robber I
        def rob_linear(houses: List[int]) -> int:
            prev_prev = houses[0]
            prev = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                cur = max(houses[i] + prev_prev, prev)
                prev_prev = prev
                prev = cur

            return prev

        # Option 1: Include first house, exclude last house (nums[:-1])
        # Option 2: Exclude first house, include last house (nums[1:])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
            