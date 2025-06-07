# Day 4 - Recursion Practice

# 1. Count the Number of Digits in an Integer Using Recursion
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("Number of digits:", count_digits(1234))  # Output: 4


# 2. Count Digits Before the Last Digit Using Recursion
def count_before_last(n):
    if n // 10 == 0:
        return 2
    return 1 + count_before_last(n // 10)

print("Digits before last:", count_before_last(12))  # Output: 1


# 3. Sum of Digits Using Recursion
def sum_of_digits(n):
    if n // 10 == 0:
        return n
    return n % 10 + sum_of_digits(n // 10)

print("Sum of digits:", sum_of_digits(157))  # Output: 13


# 4. Find the Minimum Element in a List Using Recursion
def find_min(nums):
    def rec(nums, i):
        if i == len(nums) - 1:
            return nums[i]
        minimum = rec(nums, i + 1)
        return minimum if minimum < nums[i] else nums[i]

    return rec(nums, 0)

print("Minimum element:", find_min([5, 3, 1, 9, 2]))  # Output: 1
