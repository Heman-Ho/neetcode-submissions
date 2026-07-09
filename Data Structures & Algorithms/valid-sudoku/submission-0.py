class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRow(row):
            seen = set()
            for num in row:
                if num != "." and num in seen:
                    return False
                seen.add(num)
            return True
        
        def validCol(col_idx):
            seen = set()
            for row in board:
                num = row[col_idx]
                if num != "." and num in seen:
                    return False
                seen.add(row[col_idx])
            return True
        
        # Check's if the 3x3 square of board is valid with row, col as the top left corner
        def validSquare(row, col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[row+i][col+j]
                    if num != "." and num in seen:
                        return False
                    seen.add(board[row+i][col+j])
            return True
        
        for row in board:
            if not validRow(row):
                return False
        for col in range(len(board[0])):
            if not validCol(col): 
                return False
        for i in range(0, len(board[0]), 3):
            for j in range(0, len(board), 3):
                if not validSquare(i, j):
                    return False
        return True

