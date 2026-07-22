class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def visitIsland(r, c):
            # If out of bounds or current is not unvisited land, we return 0
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return 0

            # We mark the island so that we don't visit it again
            grid[r][c] = 0

            # return 
            return 1 + visitIsland(r+1, c) + visitIsland(r-1, c) + visitIsland(r, c+1) + visitIsland(r, c-1)

        greatestArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    greatestArea = max(greatestArea, visitIsland(r,c))
        
        return greatestArea