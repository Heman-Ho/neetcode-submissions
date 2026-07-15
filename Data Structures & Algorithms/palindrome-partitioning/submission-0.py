class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur_palindromes = [] 

        def backtrack(i):
            if i >= len(s):
                res.append(cur_palindromes[:])
                return
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    cur_palindromes.append(s[i:j+1])
                    backtrack(j+1)
                    cur_palindromes.pop()
        
        def isPali(l, r):
            while l <= r: 
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0)
        return res
