class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            arr = [0]*26
            for char in s:
                arr[ord(char)-ord('a')] += 1
            key = ''.join(str(arr))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())