class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * 26
        for ss in s:
            l[ord(ss)-97] +=1
        for tt in t:
            l[ord(tt)-97] -=1
        return all(a==0 for a in l)