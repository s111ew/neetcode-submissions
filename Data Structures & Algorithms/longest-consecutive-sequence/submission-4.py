class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        # create a set to hold all unique numbers in the list
        unique_nums = set(nums)
        longest_streak = 1

        # loop through the set
        for num in unique_nums:
            # if the previous consecutive num is not in the set then it could be the start of a sequence
            if (num - 1) not in unique_nums:
                current_streak = 1
                # since we have identified the start of a sequence, we exhaust the rest of the sequence
                while (num + current_streak) in unique_nums:
                    current_streak += 1
                    longest_streak = max(longest_streak, current_streak)

        return longest_streak
        