# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


solution = Solution()

result1 = solution.containsDuplicate([1, 2, 3])
print(result1)  # False

result2 = solution.containsDuplicate([1, 2, 3, 2])
print(result2)  # True
