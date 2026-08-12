class Solution:
    def isValid(self, s: str) -> bool:
        o = ["(", "[", "{"]
        c = [")", "]", "}"]
        pairs = set([op+cl for op, cl in zip(o,c)])
        o = set(o)
        # c = set(c)
        result = []

        for i in s:
            if i in o:
                result.append(i)
            else:
                if not result or result.pop() + i not in pairs:
                    return False

        return not result