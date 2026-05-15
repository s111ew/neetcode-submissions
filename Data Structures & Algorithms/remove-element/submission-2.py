class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0
        n = len(nums)-1
        while r <= n:
            while l <= n and nums[l] != val:
                l+=1
            r = l
            while r <= n and nums[r] == val:
                r+=1
            if r <= n:
                nums[l] = nums[r]
                nums[r] = val
                r = l
        i = 0
        while i <= n and nums[i] != val:
            i+=1
        return i
