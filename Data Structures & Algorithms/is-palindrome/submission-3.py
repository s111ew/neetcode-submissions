class Solution:
    def isPalindrome(self, s):
        s_trimmed = ""
        for c in s:
          if c.isalnum():
            s_trimmed += c.lower()

        l = 0
        r = len(s_trimmed) - 1

        while l < r:
            if s_trimmed[l] != s_trimmed[r]:
                return False
            l += 1
            r -= 1

        return True
        