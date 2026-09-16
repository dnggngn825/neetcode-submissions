class Solution:
    def getKey(self, s: str) -> tuple:
        l = [0]*26
        for ch in s:
            l[ord(ch)-ord('a')]+=1
        return tuple(l)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for t in strs:
            key = self.getKey(t)
            if key in dic:
                dic[key].append(t)
            else:
                dic[key] = [t]
        return list(dic.values())