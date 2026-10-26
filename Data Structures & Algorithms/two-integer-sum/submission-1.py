class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            n = nums[i]
            key = str(target-n)
            if key in dic:
                return [dic[key], i]
            else:
                dic[str(n)] = i
        return []