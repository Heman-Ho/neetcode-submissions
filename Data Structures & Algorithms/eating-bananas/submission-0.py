class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k must be a number between 1 and the largest pile
        # we can do a binary search on those numbers 
        # by testing each time if we need a greater k or a lower k

        # A test can be done by in O(n) by summing each of math.ceil(piles[i] / k) which must be < h 
        # O(nlogn)
        if not piles:
            return 0
        l = 1
        r = max(piles)
        k = 0
        
        while l <= r:
            k = (l + r) // 2
            time_to_eat_piles = 0
            for i in range(len(piles)):
                time_to_eat_piles += (piles[i] + k - 1) // k
                if time_to_eat_piles > h:
                    break
            if time_to_eat_piles > h:
                # we need a larger eating rate
                l = k + 1
            else:
                r = k - 1

        return r + 1
        