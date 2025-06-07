# =========================== Aggressive Cows ===========================

def canWePlaceCows(arr, distance, k):
    count = 1
    last_position = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last_position >= distance:
            count += 1
            last_position = arr[i]
            
    return count >= k

def aggressiveCows(arr, k):
    arr.sort()
    low = 1
    high = arr[-1] - arr[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if canWePlaceCows(arr, mid, k):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Example usage:
# arr = [1, 2, 8, 4, 9]
# k = 3
# print(aggressiveCows(arr, k))


# =========================== Allocate Books ===========================

def canWeAllocate(maxPages, arr, k):
    no_of_pages_allocated = arr[0]
    students = 1
    for i in range(1, len(arr)):
        if arr[i] + no_of_pages_allocated <= maxPages:
            no_of_pages_allocated += arr[i]
        else:
            no_of_pages_allocated = arr[i]
            students += 1
    return students <= k

def findMinimumPages(arr, k):
    low = max(arr)
    high = sum(arr)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        if canWeAllocate(mid, arr, k):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

# Example usage:
# arr = [12, 34, 67, 90]
# k = 2
# print(findMinimumPages(arr, k))


# =========================== Stack Basics ===========================

stack = []
stack.append(10)
print(stack)
stack.append(20)
print(stack)
print(stack[-1])  # peek top of stack


# =========================== Valid Parentheses ===========================

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele in "([{":
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if (x == "(" and ele == ")") or (x == "[" and ele == "]") or (x == "{" and ele == "}"):
                    continue
                else:
                    return False
        return len(stack) == 0

# Example usage:
# sol = Solution()
# print(sol.isValid("()[]{}"))  # True
# print(sol.isValid("(]"))      # False


# =========================== Trapping Rainwater ===========================

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [-1] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i - 1])
        
        rightMax = [-1] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        
        result = 0
        for i in range(n):
            result += min(leftMax[i], rightMax[i]) - height[i]
        
        return result

# Example usage:
# sol = Solution()
# print(sol.trap([4,2,0,3,2,5]))  # Output: 9
