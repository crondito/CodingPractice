# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [1]  # add logic here


solution = Solution()

result1 = solution.twoSum([2, 7, 11, 15], 9)
print(result1)  # [0,1]

result2 = solution.twoSum([3, 2, 4], 6)
print(result2)  # [1,2]

result3 = solution.twoSum([3, 3], 6)
print(result3)  # [0,1]
