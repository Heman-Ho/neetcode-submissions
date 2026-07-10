class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We need to find the point where the number goes from high to low
        # Use a binary search if mid < nums[l], shrink right pointer to m-1
        # if mid > nums[0], move l to m + 1

        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l < r:
            check = nums[r]
            m = (l + r) // 2
        
            if nums[m] > check: 
                l = m + 1
            else:
                r = m

        return nums[l]