import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if not stones:
            return 0

        class MaxHeap: 
            def __init__(self):
                self.heap = []
            
            def insert(self, value):
                heapq.heappush(self.heap, -value)

            def pop(self):
                return -heapq.heappop(self.heap)
            
            def build_heap(self, nums):
                self.heap = [-num for num in nums]
                heapq.heapify(self.heap)
        
        heap = MaxHeap()
        heap.build_heap(stones)

        for i in range(len(stones) - 2):
            heap.insert(heap.pop() - heap.pop())

        return heap.pop() - heap.pop()