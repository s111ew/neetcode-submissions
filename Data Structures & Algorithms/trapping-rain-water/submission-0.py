class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        left_max = 0
        left = [0] * len(height)
        for i, n in enumerate(height):
            left_max = max(left_max, n)
            left[i] = left_max

        right_max = 0
        right = [0] * len(height)
        for i in range(len(height) - 1, 0, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max

        for i, n in enumerate(height):
            vol = max(0, (min(left[i], right[i]) - n))
            total += vol

        return total