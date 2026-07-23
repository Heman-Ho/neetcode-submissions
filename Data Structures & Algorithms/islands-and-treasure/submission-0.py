class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        # Every time we visit a treasure chest, we do a BFS to the surrounding land marking the shortest distance of that land to a chest
        def dfs(level, row, col):
            # Base case if out of bounds, exit
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            
            # If we find a land that is less than level, then the current search path will never be optimal
            # Thus, we can return early
            if grid[row][col] < level:
                return 
            
            # If current visited is a land, update the shortest distance
            if grid[row][col] > 0:
                grid[row][col] = level

            dfs(level+1, row+1, col)
            dfs(level+1, row-1, col)
            dfs(level+1, row, col+1)
            dfs(level+1, row, col-1)
            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    dfs(0, row, col)
        
