class Solution:
    def findMin(self, nums: List[int]) -> int:

        def findM(i,j):
            if (i==j):
                return nums[j]
            if (j == i+1):
                return nums[i] if nums[i] < nums[j] else nums[j]
            mid = int((i+j)/2)

            if (nums[i] < nums[mid] and nums[mid] < nums[j]):
                return nums[i]
            
            if (abs(nums[mid] - nums[i]) > abs(nums[j] - nums[mid])):
                return findM(i, mid)
            else:
                return findM(mid, j)
        return findM(0, len(nums)-1)