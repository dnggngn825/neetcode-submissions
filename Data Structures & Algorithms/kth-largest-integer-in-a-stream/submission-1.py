import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify_max(self.heap)
        self.n = len(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        l = heapq.nlargest(self.k, self.heap)
        return l[-1]
