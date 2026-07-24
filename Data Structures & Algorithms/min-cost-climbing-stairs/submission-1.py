class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let A[i] hold the min cost to reach the ith stair
        # A[i] = min(A[i-1] + cost(i-1), A[i-2] + cost(i-2))
        # We only need to keep track of prev 2 costs => O(1) instead of O(N) array
        if len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost)
        
        prev_prev = 0
        prev = 0

        for i in range(2, len(cost) + 1):
            cur = min(prev + cost[i-1], prev_prev + cost[i-2])
            prev_prev = prev
            prev = cur
        
        return cur

