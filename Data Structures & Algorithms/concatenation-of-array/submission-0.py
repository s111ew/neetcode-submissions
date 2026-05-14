class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * (n * 2)

        i = 0
        j = n

        while i < n:
            out[i] = nums[i]
            out[j] = nums[i]
            i += 1
            j += 1
        
        return out