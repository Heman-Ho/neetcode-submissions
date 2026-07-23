from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        
        # We run a BFS on every treasure chest in rounds
        # If it's land update it to that round's level

        coords = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    coords.append((row, col, 0))

        print(coords)

        while coords:
            row, col, distance = coords.popleft()
            # Base case
            if distance != 0 and (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != INF):
                continue
            
            grid[row][col] = distance
            coords.append((row + 1, col, distance + 1))
            coords.append((row - 1, col, distance + 1))
            coords.append((row, col + 1, distance + 1))
            coords.append((row, col - 1, distance + 1))
        



        
