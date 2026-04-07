class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        start_ptr = 0
        
        for end_ptr in range(len(s)):
            count[s[end_ptr]] = 1 + count.get(s[end_ptr], 0)
            
            max_freq = max(max_freq, count[s[end_ptr]])
            
            while (end_ptr - start_ptr + 1) - max_freq > k:
                count[s[start_ptr]] -= 1
                start_ptr += 1
            
            max_length = max(max_length, end_ptr - start_ptr + 1)
            
        return max_length