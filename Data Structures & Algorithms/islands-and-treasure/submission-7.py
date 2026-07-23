from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        
        # We run a BFS on every treasure chest in rounds using a queue
        # If it's land update it's distance

        coords = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    coords.append((row, col))

        print(coords)

        while coords:
            row, col = coords.popleft()
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in neighbors:
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != INF: 
                    continue
                grid[r][c] = grid[row][col] + 1
                coords.append((r, c))
     



        
