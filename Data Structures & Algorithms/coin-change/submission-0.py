class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        # Let A[i] be the fewest number of coins it takes to make up j (-1 if impossible)
        # Initiate A[0] = 0, A[coin] = 1 for coin in coins
        # A[i] = min(A[i-coin] + 1, for coin in coins)

        A = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin < amount + 1:
                A[coin] = 1
        A[0] = 0

        for i in range(1, amount + 1): 
            if A[i] == 1:
                continue
            cur_min = float('inf')
            for coin in coins: 
                if coin < i: 
                    cur_min = min(cur_min, A[i-coin])
            A[i] = cur_min + 1
        
        if A[amount] != float('inf'):
            return A[amount]
        else:
            return -1

                    



