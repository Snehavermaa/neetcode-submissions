class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t or len(s)!=len(t) or s.count(i)!=t.count(i):
                return False
        return True