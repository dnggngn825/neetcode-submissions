import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            s = str(num)
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        
        heap = [(-value, key) for key,value in dic.items()]
        heapq.heapify(heap)
        result = []
        while k > 0:
            item = heapq.heappop(heap)
            k-= 1
            if (item):
                result.append(int(item[1]))
        return result