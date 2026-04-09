class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2

            if nums[right] < nums[mid]:
                left = mid + 1

            else:
                right = mid
        
        return nums[left]
