class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Do a binary search to find the correct row, then search the row again with binary search to see if it exists
        top = 0 
        bottom = len(matrix) - 1
        mid = 0

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        else:
            return False
        
        row = mid
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False


