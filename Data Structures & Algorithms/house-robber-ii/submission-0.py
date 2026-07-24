class Solution:
    def rob(self, nums: List[int]) -> int:
        # We split the circle into two lines: 
        # 1. the line includes house 0 and excludes house n - 1
        # 2. the line excludes house 0 and includes house n
        # This ensures we meet the circle constraint

        # Handle edge cases
        if len(nums) <= 3:
            return max(nums)

        # Find the max from both lines
        ret = 0

        # For each line
        for i in range(2):
            # Let A[i] = the max amount of money that a robber can rob from the first i houses 
            # A[i] = max(nums[i] + A[i-2], A[i-1])
            # We only need to keep track of the value from the previous 2 houses so we don't need to keep track of the whole array
            prev_prev = nums[i]
            prev = max(nums[i], nums[i+1])

            # First loop: we visit house 2 to house n-2 (0 indexed)
            # Second loop: we visit house 3 to house n-1 (0 indexed)
            for j in range(i+2, i + len(nums) - 1):
                cur = max(nums[j] + prev_prev, prev)
                prev_prev = prev
                prev = cur
            ret = max(ret, cur)
        return ret
            
            