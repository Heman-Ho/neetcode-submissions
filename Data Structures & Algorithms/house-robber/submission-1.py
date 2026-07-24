class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let A[i] be the max amount of money you can rob from the first i houses
        # A[i] = max(nums[i] + A[i-2], A[i-1)]
        # We only need to keep track of prev 3 houses max robbery
        # Initially A[0] = nums[0] and A[1] = max(nums[0], nums[1]

        # edge cases
        if len(nums) <= 2:
            return max(nums)  

        prev_prev = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(nums[i] + prev_prev, prev)
            prev_prev = prev
            prev = cur
        
        return cur