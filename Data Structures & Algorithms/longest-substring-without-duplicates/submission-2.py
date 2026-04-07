class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0
        if length == 1:
            return 1

        curr_chars = {s[0]}
        curr_max = 1
        ptr_start = 0
        ptr_end = 1
        while ptr_end < length:
            if s[ptr_end] not in curr_chars:
                curr_chars.add(s[ptr_end])
                ptr_end += 1
            else:
                curr_chars.remove(s[ptr_start])
                ptr_start += 1
            curr_max = max(curr_max, len(curr_chars))
        return curr_max