class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n_to_eval = nums[abs(n) - 1]
            if n_to_eval < 0:
                return abs(n)
            nums[abs(n) - 1] = n_to_eval * -1
            