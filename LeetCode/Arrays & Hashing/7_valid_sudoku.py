# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = np.array(board)
        transposed_arr = arr.transpose()

        if not self.check_no_repeated_numbers(arr):
            return False

        if not self.check_no_repeated_numbers(transposed_arr):
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                aux_arr = arr[i : i + 3, j : j + 3]
                values = set()
                for element in aux_arr.flatten():
                    if element.isdigit() and element in values:
                        return False
                    values.add(element)

        return True

    def check_no_repeated_numbers(self, arr: np.array) -> bool:
        for column in arr:
            filtered_column = column[np.char.isnumeric(column)]
            numeric_column = filtered_column.astype(int)
            if len(np.unique(numeric_column)) != len(numeric_column):
                return False

        return True


solution = Solution()

result1 = solution.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(result1)  # True

result2 = solution.isValidSudoku(
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(result2)  # False

result3 = solution.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "8", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", "2", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(result3)  # False
