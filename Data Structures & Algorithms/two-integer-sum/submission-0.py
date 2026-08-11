class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            f = target - nums[i]
            if (f) in s:
                return [s[f], i]
            else:
                s[nums[i]] = i
            