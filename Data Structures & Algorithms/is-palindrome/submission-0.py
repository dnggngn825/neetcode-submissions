class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s.lower() if x.isalnum()]

        i,j = 0, len(s)-1
        while i<j:
            if (s[i] != s[j]):
                return False
            else:
                i+=1
                j-=1
        return True