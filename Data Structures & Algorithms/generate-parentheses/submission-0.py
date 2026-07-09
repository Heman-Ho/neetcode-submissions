class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []
        
        def dfs(left_count, right_count):
            # base case
            if len(comb) == n*2:
                res.append("".join(comb))
                return
            
            # Constraints:
            # we need to have more lefts than rights always 
            # We must have no more than n left parentheses
         
            if left_count > 0:
                comb.append("(")
                dfs(left_count-1, right_count+1)
                comb.pop()
            if right_count > 0:
                comb.append(")")
                dfs(left_count, right_count-1)
                comb.pop()
        
        dfs(n, 0)
        return res

