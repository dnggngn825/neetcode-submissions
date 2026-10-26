import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==0:
            return []
        dic = {}
        for n in nums:
            if str(n) in dic:
                dic[str(n)] += 1
            else:
                dic[str(n)] = 1
        
        l = [(-1*value, key) for key,value in dic.items()]
        heapq.heapify(l)
        result = []

        while k > 0:
            node = heapq.heappop(l)
            result.append(int(node[1]))
            k-=1
        return result