class Solution:
    def climbStairs(self, n: int) -> int:
        # Let A[i] represent the how many ways to reach the ith step
        # A[i] = A[i-1] + A[i-2]

        # notice that we only need to keep track of the last 2 steps to calculate he current
        if n <= 2:
            return n

        prev = 2
        prev2 = 1
        for i in range(2, n):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return cur
            