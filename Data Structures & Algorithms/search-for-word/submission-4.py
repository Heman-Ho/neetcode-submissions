class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(x, y, i):
            # Base case
            if i >= len(word): 
                return True
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False
            if (x,y) in visited:
                return False
            if board[y][x] != word[i]:
                return False
            
            visited.add((x,y))
            res = (dfs(x+1, y, i+1) or 
                   dfs(x-1, y, i+1) or 
                   dfs(x, y+1, i+1) or 
                   dfs(x, y-1, i+1))
            visited.remove((x,y))
            return res 

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(col, row, 0):
                    return True
        return False
            