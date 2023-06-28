# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        return list(anagram_groups.values())


solution = Solution()

result1 = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result1)  # [["bat"],["nat","tan"],["ate","eat","tea"]]

result2 = solution.groupAnagrams([""])
print(result2)  # [[""]]

result3 = solution.groupAnagrams(["a"])
print(result3)  # [["a"]]
