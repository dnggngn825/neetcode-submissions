class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        
        if (n == 0):
            return 0
        longest = 0
        j=1
        substring = set()
        substring.add(s[i])
        while True:
            while j < n and s[j] not in substring:
                substring.add(s[j])
                j+=1
            if (j-i>longest):
                longest = j-i
            if (j == n):
                return longest
            while s[j] in substring:
                substring.remove(s[i])
                i+=1
        return longest
        