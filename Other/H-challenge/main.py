# Calculate the sum of squares of given integers, excluding any negatives.
#
# The first line of the input will be an integer N (1 <= N <= 100),
# indicating the number of test cases to follow.
#
# Each of the test cases will consist of a line with an integer X (0 < X <= 100),
# followed by another line consisting of X number of space-separated integers
# Yn (-100 <= Yn <= 100).
#
# For each test case, calculate the sum of squares of the integers,
# excluding any negatives, and print the calculated sum in the output.
#
# Note: There should be no output until all the input has been received.
# Note 2: Do not put blank lines between test cases solutions.
# Note 3: Take input from standard input, and output to standard output.
# Note 4: Do not use any for loop, while loop, or any list / set / dictionary comprehension.
# Note 5: Use standard libraries
# Note 6: Do not declare global variables

import sys


def sum_of_squares(nums):
    if not nums:
        return 0
    elif nums[0] < 0:
        return sum_of_squares(nums[1:])
    else:
        return nums[0] ** 2 + sum_of_squares(nums[1:])


def process_case():
    num_integers = int(sys.stdin.readline().strip())
    integers = list(map(int, sys.stdin.readline().strip().split()[:num_integers]))
    result = sum_of_squares(integers)
    return result


def main():
    num_test_cases = int(sys.stdin.readline().strip())
    results = list(map(lambda _: process_case(), range(num_test_cases)))

    list(map(print, results))


if __name__ == "__main__":
    main()
