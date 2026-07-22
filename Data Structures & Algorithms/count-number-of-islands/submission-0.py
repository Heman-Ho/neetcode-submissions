class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def searchIsland(r, c):
            nonlocal ROWS
            nonlocal COLS
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            searchIsland(r+1,c)
            searchIsland(r-1,c)
            searchIsland(r,c+1)
            searchIsland(r,c-1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    searchIsland(r, c)
        return count
