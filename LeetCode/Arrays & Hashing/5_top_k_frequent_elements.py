# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


solution = Solution()

result1 = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result1)  # [1,2]

result2 = solution.topKFrequent([1], 1)
print(result2)  # [1]

result3 = solution.topKFrequent([3, 0, 1, 0], 1)
print(result3)  # [0]
