# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


solution = Solution()

result1 = solution.isAnagram("anagram", "nagaram")
print(result1)  # True

result2 = solution.isAnagram("rat", "car")
print(result2)  # False

result2 = solution.isAnagram("aacc", "ccac")
print(result2)  # False
