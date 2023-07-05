# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        return False # TO DO
    
solution = Solution()

result1 = solution.isValid("()")
print(result1)  # True

result2 = solution.isValid("()[]{}")
print(result2)  # True

result3 = solution.isValid("(]")
print(result3)  # False