class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = right = 1
        n = len(nums)
        result = [1]*n
        for i in range(n):
            result[i] = left
            left = left*nums[i]
        for t in range(n-1,-1,-1):
            result[t] = result[t]*right
            right = right*nums[t]
        return result