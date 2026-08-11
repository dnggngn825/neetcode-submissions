class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dic = {0: [[]]}
        for i in range(len(nums)):
            dic[i+1] = dic[i] + [d + [nums[i]] for d in dic[i]]
        return dic[i+1]