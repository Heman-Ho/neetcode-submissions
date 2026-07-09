class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a sliding window. When we first reach a duplicate letter in the 
        # window, move the left pointer past the duplicate letter, to continue the search
        # We can keep track of all the letters and their corresponding index in a dict
        longest = 0
        l = 0
        r = 0
        c_indices = {}

        while r < len(s):
            if s[r] in c_indices: 
                l = max(l, c_indices[s[r]] + 1)
            c_indices[s[r]] = r
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest