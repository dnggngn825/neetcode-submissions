import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==0:
            return []
        dic = Counter(nums)
        
        l = [(-1*value, key) for key,value in dic.items()]
        heapq.heapify(l)
        result = []

        while k > 0:
            node = heapq.heappop(l)
            result.append(node[1])
            k-=1
        return result