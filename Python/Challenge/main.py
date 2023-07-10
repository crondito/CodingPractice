def sum_of_squares(nums):
    if not nums:
        return 0
    elif nums[0] < 0:
        return sum_of_squares(nums[1:])
    else:
        return nums[0] ** 2 + sum_of_squares(nums[1:])


def process_case():
    num_integers = int(input().strip())
    integers = list(map(int, input().strip().split()[:num_integers]))
    return sum_of_squares(integers)


def main():
    num_test_cases = int(input().strip())
    results = list(map(lambda _: process_case(), range(num_test_cases)))
    list(map(print, results))


if __name__ == "__main__":
    main()
