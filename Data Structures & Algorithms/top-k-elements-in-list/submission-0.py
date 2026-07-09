from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        ret = []
        frequencies = Counter(nums)
        buckets = [[] for _ in range(len(nums))]
        for num in frequencies:
            buckets[frequencies[num]-1].append(num)
        
        cur_nums = 0
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ret.append(num)
                cur_nums += 1
                if cur_nums == k:
                    return ret
