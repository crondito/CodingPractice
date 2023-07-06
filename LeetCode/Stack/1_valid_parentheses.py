# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

from typing import List

class Solution:
    def check_parentheses(self, lst: List[str]):
        stack = []
        opening_chars = "({["
        closing_chars = ")}]"
        matching_chars = {")": "(", "]": "[", "}": "{"}

        for element in lst:
            if element in opening_chars:
                stack.append(element)
            elif element in closing_chars:
                if len(stack) == 0 or stack[-1] != matching_chars[element]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        return self.check_parentheses(list(s))
    
    
    
solution = Solution()

result1 = solution.isValid("()")
print(result1)  # True

result2 = solution.isValid("()[]{}")
print(result2)  # True

result3 = solution.isValid("(]")
print(result3)  # False

result4 = solution.isValid(")(")
print(result4)  # False