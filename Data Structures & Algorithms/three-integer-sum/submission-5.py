class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First sort the list of nums
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -num
            l = i + 1
            r = len(nums) - 1

            while l < r:
                guess = nums[l] + nums[r]
                if guess > target:
                    r -= 1
                elif guess < target:
                    l += 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    res.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l+=1

        return res  