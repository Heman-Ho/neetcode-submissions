class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Use a sliding winidow of size s1. 
        # Use a dictionary to check if its a permutation
        if len(s1) > len(s2):
            return False

        s1_freqs = {}
        for letter in s1:
              s1_freqs[letter] = s1_freqs.get(letter, 0) + 1

        window_freqs = {}
        l = 0
        r = len(s1)

        for i in range(r):
            letter = s2[i]
            window_freqs[letter] = window_freqs.get(letter, 0) + 1

        if window_freqs == s1_freqs:
                return True

        while r < len(s2):
            if window_freqs[s2[l]] == 1:
                del window_freqs[s2[l]]
            else:
                window_freqs[s2[l]] -= 1
            window_freqs[s2[r]] = window_freqs.get(s2[r], 0) + 1
            if window_freqs == s1_freqs:
                return True
            
            l += 1
            r += 1
        return False