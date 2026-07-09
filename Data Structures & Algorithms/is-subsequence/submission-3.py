class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        l, r = 0, 0

        while l < len(s):
            # exit early
            if (len(s) - l) > (len(t) - r) or r >= len(t):
                return False

            while s[l] != t[r]:
                r += 1
                if r >= len(t):
                    return False
            l += 1
            r += 1

            
            

        return True
            

        