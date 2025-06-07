# 1. Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 2. Lower Bound (first position where target could be inserted)
def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# 3. Upper Bound (first position greater than target)
def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# 4. Search Insert Position (same as lower bound)
def search_insert_position(arr, target):
    return lower_bound(arr, target)

# 5. Floor and Ceiling
def get_floor_and_ceil(arr, x):
    def get_floor(arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def get_ceil(arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    floor = get_floor(arr, x)
    ceil = get_ceil(arr, x)
    return [floor, ceil]

# 6. Find first and last position of an element in a sorted array
def search_range(nums, target):
    def get_lower_bound(nums, target):
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def get_upper_bound(nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    lb = get_lower_bound(nums, target)
    if lb == -1 or lb >= len(nums) or nums[lb] != target:
        return [-1, -1]
    ub = get_upper_bound(nums, target) - 1
    return [lb, ub]

# 7. Search in Rotated Sorted Array
def search_in_rotated_sorted(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if arr[mid] <= key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# 8. Count number of rotations in rotated sorted array
def count_rotations(arr):
    low, high = 0, len(arr) - 1
    min_val = float('inf')
    min_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            if arr[low] < min_val:
                min_val = arr[low]
                min_index = low
            low = mid + 1
        else:
            if arr[mid] < min_val:
                min_val = arr[mid]
                min_index = mid
            high = mid - 1
    return min_index
