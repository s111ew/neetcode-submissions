class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s) - 1 
        l = 0
        r = 1
        total = 0
        while r <= n:
            total += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1
        return total