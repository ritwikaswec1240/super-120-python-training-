# Day 5 - Array Problems: Two Sum, Three Sum, Majority Element, Four Sum

from typing import List
from collections import defaultdict

# ------------------------------
# 1. Two Sum
# ------------------------------

# Method 1: Brute Force
class TwoSumMethod1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Method 2: Hashmap
class TwoSumMethod2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i

# Method 3: Two-pointer approach (when array is sorted)
def twoSumSorted(nums, target):
    nums.sort()
    low, high = 0, len(nums) - 1
    while low < high:
        s = nums[low] + nums[high]
        if s == target:
            return "yes"
        elif s > target:
            high -= 1
        else:
            low += 1
    return "no"


# ------------------------------
# 2. Three Sum
# ------------------------------

# Method 1: Brute Force with Set
class ThreeSumMethod1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_sum = set()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet_sum.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in triplet_sum]

# Method 2: Hashmap
class ThreeSumMethod2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_sum = set()
        n = len(nums)
        for i in range(n - 1):
            hashmap = set()
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                if complement in hashmap:
                    triplet_sum.add(tuple(sorted([nums[i], nums[j], complement])))
                hashmap.add(nums[j])
        return [list(t) for t in triplet_sum]

# Method 3: Two-pointers after sorting
class ThreeSumMethod3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


# ------------------------------
# 3. Majority Element (> n//2)
# ------------------------------

class MajorityElement1:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for key, value in d.items():
            if value > n // 2:
                return key


# ------------------------------
# 4. Majority Element II (> n//3)
# ------------------------------

class MajorityElement2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return [key for key, value in d.items() if value > n // 3]


# ------------------------------
# 5. Four Sum
# ------------------------------

# Method 1: Hashing
class FourSumMethod1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        pair_sum = defaultdict(list)
        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                pair_sum[nums[i] + nums[j]].append((i, j))

        for i in range(n):
            for j in range(i + 1, n):
                complement = target - nums[i] - nums[j]
                for a, b in pair_sum.get(complement, []):
                    if b < i:
                        quad = tuple(sorted([nums[a], nums[b], nums[i], nums[j]]))
                        result.add(quad)
        return [list(q) for q in result]

# Method 2: Two pointers (sorted + nested loops)
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result
