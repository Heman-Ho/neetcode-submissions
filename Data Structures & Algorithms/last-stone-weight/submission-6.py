import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
    
        return -stones[0]