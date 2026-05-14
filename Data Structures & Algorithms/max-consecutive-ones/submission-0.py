class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        curr_len = 0
        for n in nums:
            if n == 1:
                curr_len += 1
                curr_max = max(curr_max, curr_len)
            else:
                curr_len = 0
        
        return curr_max