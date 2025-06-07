# #  204. Count Primes
# # 📌 Prime number
# # A number that has only 2 factors (1 and the number itself)
# Examples: 2, 3, 5, 7, 11, 13...

# # 🚀 Basic Solution — O(n²)
# def countPrimes(self, n: int) -> int:
#     def is_prime(num):
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         return count == 2

#     count = 0
#     for i in range(2, n):
#         if is_prime(i):
#             count += 1
#     return count
# # 🚀 Optimized Solution — O(n * sqrt(n))
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         def is_prime(num):
#             count = 0
#             for i in range(1, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     count += 2
#             return count == 2

#         count = 0
#         for i in range(2, n):
#             if is_prime(i):
#                 count += 1
#         return count
# # 🚀 Most Optimized — O(n log log n)
# Sieve of Eratosthenes

# def countPrimes(self, n: int) -> int:
#     prime = [1] * n

#     for i in range(2, int(n ** 0.5) + 1):
#         if prime[i] == 1:
#             for j in range(i * i, n, i):
#                 prime[j] = 0

#     count = 0
#     for i in range(2, n):
#         if prime[i] == 1:
#             count += 1
#     return count
# # 🟢 74. Search in 2D Matrix
# # 📌 O(n + m)
# def searchMatrix(matrix, target):
#     n = len(matrix)
#     m = len(matrix[0])

#     row = 0
#     col = m - 1

#     while row < n and col >= 0:
#         if matrix[row][col] == target:
#             return True
#         elif target < matrix[row][col]:
#             col -= 1
#         else:
#             row += 1

#     return False