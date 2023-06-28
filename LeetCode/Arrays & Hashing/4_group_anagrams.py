# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return strs  # TO DO


solution = Solution()

result1 = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result1)  # [["bat"],["nat","tan"],["ate","eat","tea"]]

result2 = solution.groupAnagrams([""])
print(result2)  # [[""]]

result3 = solution.groupAnagrams(["a"])
print(result3)  # [["a"]]
