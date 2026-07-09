from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        ret = []
        frequencies = Counter(nums)
        buckets = [[] for _ in range(len(nums))]
        for num, freq in frequencies.items():
            buckets[freq-1].append(num)
        
       
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
