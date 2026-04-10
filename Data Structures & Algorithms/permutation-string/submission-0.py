class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars_to_find = {}
        chars_in_window = {}

        for i in range(len(s1)):
            if s1[i] not in chars_to_find:
                chars_to_find[s1[i]] = 1
            else:
                chars_to_find[s1[i]] += 1

        for i in range(len(s1)):
            if s2[i] not in chars_in_window:
                chars_in_window[s2[i]] = 1
            else:
                chars_in_window[s2[i]] += 1

        if chars_to_find == chars_in_window:
                return True

        start = 0
        end = len(s1) - 1

        while end < len(s2) - 1:
            if chars_in_window[s2[start]] > 1:
                chars_in_window[s2[start]] -= 1
            else:
                del chars_in_window[s2[start]]

            start += 1
            end += 1

            if s2[end] not in chars_in_window:
                chars_in_window[s2[end]] = 1
            else:
                chars_in_window[s2[end]] += 1
            
            if chars_to_find == chars_in_window:
                return True
        
        return False