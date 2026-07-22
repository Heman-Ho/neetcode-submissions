class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        # Invalidate entire island
        def searchIsland(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            searchIsland(r+1,c)
            searchIsland(r-1,c)
            searchIsland(r,c+1)
            searchIsland(r,c-1)
            
        # When we encounter an island, we increment count
        # and invalidate the entire island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    searchIsland(r, c)
        return count
