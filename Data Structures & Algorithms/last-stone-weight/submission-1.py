import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = [-s for s in stones]
        heapq.heapify(l)
        n = len(l)

        while n:
            if (n == 1):
                return -heapq.heappop(l)
            else:
                a, b = -heapq.heappop(l), -heapq.heappop(l)
                if (a!=b):
                    heapq.heappush(l, -abs(a-b))
            n = len(l)
        return 0