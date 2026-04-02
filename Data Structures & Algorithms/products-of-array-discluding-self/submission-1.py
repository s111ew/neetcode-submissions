class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [0] * length
        left = 1
        right = 1
        # left pass
        for i in range(length):
            ans[i] = left
            left *= nums[i]

        for i in range(len(ans)-1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
        