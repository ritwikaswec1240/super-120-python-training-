# =========================== 1004. Max Consecutive Ones III ===========================

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        maxLen = 0      
        count_zeros = 0

        while right < n:
            if nums[right] == 0:
                count_zeros += 1
            if count_zeros > k:
                while count_zeros > k:
                    if nums[left] == 0:
                        count_zeros -= 1
                    left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen


# =========================== 904. Fruits Into Baskets (Brute Force) ===========================

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        maxLen = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(fruits[j])
                if len(s) > 2:
                    break
                maxLen = max(maxLen, j - i + 1)
        return maxLen


# =========================== 904. Fruits Into Baskets (Sliding Window) ===========================

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        right = 0 
        maxLen = 0
        d = {}

        while right < n:
            d[fruits[right]] = d.get(fruits[right], 0) + 1

            if len(d) > 2:
                while len(d) > 2:
                    d[fruits[left]] -= 1
                    if d[fruits[left]] == 0:
                        del d[fruits[left]]
                    left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen


# =========================== 53. Maximum Subarray (Kadane's Algorithm) ===========================

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        n = len(nums)
        maxSum = float("-inf")
        currentSum = 0

        for i in nums:
            currentSum += i
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
                
        return maxSum


# =========================== Longest Subarray With Sum K ===========================

def longestSubarrayWithSumK(arr, k):
    d = {}
    sum = 0
    maxLen = 0
    n = len(arr)

    for i in range(n):
        sum += arr[i]

        if sum == k:
            maxLen = i + 1

        rem = sum - k
        if rem in d:
            maxLen = max(maxLen, i - d[rem])

        if sum not in d:
            d[sum] = i

    return maxLen
