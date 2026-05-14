class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        s.reverse()
        
        for c in t:
            if len(s) == 0:
                return True
                
            if c == s[-1]:
                s.pop()

        return len(s) == 0