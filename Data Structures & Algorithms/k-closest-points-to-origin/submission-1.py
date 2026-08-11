import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(NlogN) time
        # return sorted(points, key=lambda x: math.sqrt(x[0]**2 + x[1]**2))[:k]

        l = []
        heapq.heapify(l)
        size = 0
        for x in points:
            heapq.heappush(l, (-math.sqrt(x[0]**2 + x[1]**2), x))
            size += 1
            if (size > k):
                heapq.heappop(l)
        return list(map(lambda x:x[1], l))