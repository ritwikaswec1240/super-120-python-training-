#koko eating bananas 
# #Brute force version
from math import ceil

class Solution:
    def kokoEat(self, arr, k):
        for noOfBanana in range(1, max(arr) + 1):
            total_time = 0
            for num in arr:
                total_time += ceil(num / noOfBanana)
            if total_time <= k:
                return noOfBanana

# Example usage
arr = [3, 6, 7, 11]
k = 8
sol = Solution()
print(sol.kokoEat(arr, k))   # Output: 4


# Optimized version (binary search):
from math import ceil

class Solution:
    def kokoEat(self, arr, k):
        low = 1
        high = max(arr)
        
        while low < high:
            mid = (low + high) // 2
            total_time = 0
            for num in arr:
                total_time += ceil(num / mid)
            
            if total_time <= k:
                high = mid  # Try slower eating speed
            else:
                low = mid + 1  # Need faster eating speed
        
        return low

# Example usage
arr = [3, 6, 7, 11]
k = 8
sol = Solution()
print(sol.kokoEat(arr, k))   # Output: 4
