class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] *26
        for ch in s:
            array[ord(ch)-ord('a')] +=1
        for ch in t:
            array[ord(ch)-ord('a')] -=1
        return all([check == 0 for check in array])