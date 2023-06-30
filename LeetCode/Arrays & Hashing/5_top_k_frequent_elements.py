# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return []  # TO DO


solution = Solution()

result1 = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result1)  # [1,2]

result2 = solution.topKFrequent([1], 1)
print(result2)  # [1]
