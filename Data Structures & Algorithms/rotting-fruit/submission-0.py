from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # For all rotten fruit at the beginning:
        # run a simultaneous BFS on each rotting fruit, counting each minute for every level of the BFS
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        # simultaneous BFS
        clock = 0
        while q:
            row, col, minute = q.popleft()
            neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
            for r, c in neighbors:
                # Base case we don't continue the BFS if out of bound or if not a fresh fruit
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                    continue
                # the fruit rots in this minute, update the state
                grid[r][c] = 2

                # continue the BFS on newly rotted fruits
                clock = minute + 1
                q.append((r, c, clock))
    
        # Do a final search of the grid to see if any fresh fruit still exists
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return clock