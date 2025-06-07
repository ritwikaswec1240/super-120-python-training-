# =========================== Generate Subarrays ===========================

arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    for j in range(i, n):
        print(arr[i:j+1])


# =========================== Subarray of Max Sum of Length k ===========================

arr = list(map(int, input().split()))
k = int(input())
n = len(arr)
maxSum = 0
left = 0
right = k - 1

Sum = sum(arr[left:right + 1])
maxSum = Sum

while right < n - 1:
    Sum -= arr[left]
    left += 1
    right += 1
    Sum += arr[right]
    maxSum = max(maxSum, Sum)

print(maxSum)


# =========================== Max Length of Subarray with Sum ≤ K (Brute Force) ===========================

arr = list(map(int, input().split()))
k = int(input())
n = len(arr)
maxLen = 0

for i in range(n):
    for j in range(i, n):
        if sum(arr[i:j+1]) <= k:
            maxLen = max(maxLen, j - i + 1)

print(maxLen)


# =========================== Max Length of Subarray with Sum ≤ K (Sliding Window) ===========================

arr = list(map(int, input().split()))
k = int(input())
n = len(arr)
maxLen = 0
Sum = 0
left = 0

for right in range(n):
    Sum += arr[right]
    while Sum > k:
        Sum -= arr[left]
        left += 1
    maxLen = max(maxLen, right - left + 1)

print(maxLen)


# =========================== 1423. Maximum Points You Can Obtain from Cards ===========================

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftSum = sum(cardPoints[:k])
        maxSum = leftSum
        rightSum = 0
        rightIndex = n - 1

        for i in range(k - 1, -1, -1):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[rightIndex]
            maxSum = max(maxSum, leftSum + rightSum)
            rightIndex -= 1

        return maxSum


# =========================== 3. Longest Substring Without Repeating Characters (Brute Force) ===========================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        for i in range(n):
            checker = [0] * 256
            for j in range(i, n):
                if checker[ord(s[j])] == 1:
                    break
                checker[ord(s[j])] = 1
                maxLen = max(maxLen, j - i + 1)
        return maxLen


# =========================== 3. Longest Substring Without Repeating Characters (Optimized Sliding Window) ===========================

s = input()
n = len(s)
left = 0
right = 0
maxLen = 0
d = {}

while right < n:
    if s[right] in d and d[s[right]] >= left:
        left = d[s[right]] + 1
    d[s[right]] = right
    maxLen = max(maxLen, right - left + 1)
    right += 1

print(maxLen)


# =========================== 1004. Max Consecutive Ones III ===========================

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        maxLen = 0
        zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)

        return maxLen
