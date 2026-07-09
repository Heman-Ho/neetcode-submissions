class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l and r pointer
        # keep track of max area so far
        # if the left wall is taller than the right wall, any area that uses the left wall will be better than any area using the right wall.   
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)
            if heights[l] > heights[r]: 
                r -= 1
            else:
                l += 1
        return max_area