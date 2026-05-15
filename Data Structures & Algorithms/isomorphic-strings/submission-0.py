class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        i = 0
        n = len(s)-1
        while i <= n:
            if s[i] not in st:
                st[s[i]] = t[i]
            else:
                if st[s[i]] != t[i]:
                    return False

            if t[i] not in ts:
                ts[t[i]] = s[i]
            else:
                if ts[t[i]] != s[i]:
                    return False
            i+=1
        return True
            