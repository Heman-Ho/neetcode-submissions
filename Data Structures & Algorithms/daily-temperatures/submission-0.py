class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono = [(temperatures[0], 0)]
        for idx in range(1, len(temperatures)): 
            temp = temperatures[idx]
            while mono and temp > mono[-1][0]:
                cur = mono.pop()
                res[cur[1]] = idx - cur[1]
            mono.append((temp, idx))
        return res
