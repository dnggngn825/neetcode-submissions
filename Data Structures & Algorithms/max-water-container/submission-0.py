class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        i,j = 0, len(heights)-1
        while i<j:
            if (heights[i] > heights[j]):
                maxA = max(maxA, heights[j] * (j-i))
                j-=1
            else:
                maxA = max(maxA, heights[i] * (j-i))
                i+=1
        return maxA