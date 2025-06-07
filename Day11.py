 # koko eating 
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
