class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Do a binary search to find the correct row, then search the row again with binary search to see if it exists
        l = 0 
        r = len(matrix) - 1
        m = 0

        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                break
        
        row = m
        l = 0
        r = len(matrix[0]) - 1
        
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False


