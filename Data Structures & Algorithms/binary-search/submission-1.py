class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            # m = (l + r) // 2
            # To prevent overflow use this equation instead of the above one
            m = l + (r - l) // 2
            if nums[m] == target: 
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1