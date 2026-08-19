import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if (n == 2 or n == 1):
            if (target not in nums):
                return -1
            else:
                return 1 if nums[0] != target else 0
        
        pivot = math.floor(n/2)
        index = -1
        
        if (nums[pivot] == target):
            return pivot

        if (nums[pivot] > target):
            index = self.search(nums[:pivot], target)
        else:
            index = pivot + self.search(nums[pivot:], target) if self.search(nums[pivot:], target) != -1 else -1

        return index
