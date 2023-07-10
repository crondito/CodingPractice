# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        changed_s = re.sub(r"[\W_]+", "", s.lower())
        return changed_s == changed_s[::-1]


solution = Solution()

result1 = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result1)  # True

result2 = solution.isPalindrome("race a car")
print(result2)  # False

result3 = solution.isPalindrome(" ")
print(result3)  # True

result4 = solution.isPalindrome("ab_a")
print(result4)  # True
