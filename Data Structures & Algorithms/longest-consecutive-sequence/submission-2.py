class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0
        c = set()
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] not in c and nums[i]-1 not in s:
                count = 1
                check = nums[i] +1
                while check in s:
                    count+=1
                    c.add(nums[i])
                    check+=1
                maxCount = max(maxCount, count)
            
            i+=1
        return maxCount