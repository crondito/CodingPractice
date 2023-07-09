# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[i] = num
        for i in range(len(num_dict)):
            for j in range(i + 1, len(num_dict)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()

result1 = solution.twoSum([2, 7, 11, 15], 9)
print(result1)  # [0,1]

result2 = solution.twoSum([3, 2, 4], 6)
print(result2)  # [1,2]

result3 = solution.twoSum([3, 3], 6)
print(result3)  # [0,1]
