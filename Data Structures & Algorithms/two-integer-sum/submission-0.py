class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Insert each num's complement (target - num) into a dictionary, and it's index
        complements = {}
        for i, num in enumerate(nums): 
            if num in complements:
                return [complements[num], i]
            complements[target - num] = i
        return []