class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t = list(t)
        t.reverse()

        for c in s:
            if len(t) == 0:
                return 0
            
            if c == t[-1]:
                t.pop()
            
        return len(t)