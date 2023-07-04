# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


solution = Solution()

result1 = solution.longestConsecutive([100, 4, 200, 1, 3, 2])
print(result1)  # 4

result2 = solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(result2)  # 9
