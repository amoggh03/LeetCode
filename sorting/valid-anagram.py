class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in t:
                return False
            else:
                t = t.replace(i,"", 1)
                continue
        return True