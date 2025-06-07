#Merge two sorted arrays

#Merge sort

#Quick sort (fixed bugs)

#Selection sort

#Bubble sort

#Insertion sort
from typing import List

# 1. Merge Two Sorted Arrays
def merge_two_sorted_arrays(num1: List[int], num2: List[int]) -> List[int]:
    i, j = 0, 0
    result = []
    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            result.append(num1[i])
            i += 1
        else:
            result.append(num2[j])
            j += 1
    while i < len(num1):
        result.append(num1[i])
        i += 1
    while j < len(num2):
        result.append(num2[j])
        j += 1
    return result

# 2. Merge Sort
def merge_sort(arr: List[int]) -> List[int]:
    def ms(arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        ms(arr, low, mid)
        ms(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        for idx, val in enumerate(temp):
            arr[low + idx] = val

    ms(arr, 0, len(arr) - 1)
    return arr

# 3. Quick Sort
def quick_sort(arr: List[int]) -> List[int]:
    def qS(arr, low, high):
        if low < high:
            pIndex = partition(arr, low, high)
            qS(arr, low, pIndex - 1)
            qS(arr, pIndex + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i > j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    qS(arr, 0, len(arr) - 1)
    return arr

# 4. Selection Sort
def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        Min = i
        for j in range(i + 1, n):
            if arr[j] < arr[Min]:
                Min = j
        arr[i], arr[Min] = arr[Min], arr[i]
    return arr

# 5. Bubble Sort
class BubbleSortSolution:
    def bubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# 6. Insertion Sort
class InsertionSortSolution:
    def insertionSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            while i > 0 and arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1
        return arr

# ---------------- Example usage ----------------
if __name__ == "__main__":
    print("Merge two sorted arrays:")
    print(merge_two_sorted_arrays([1,3,5], [2,4,6]))

    print("\nMerge sort:")
    print(merge_sort([5, 2, 9, 1, 5, 6]))

    print("\nQuick sort:")
    print(quick_sort([5, 2, 9, 1, 5, 6]))

    print("\nSelection sort:")
    print(selection_sort([29, 10, 14, 37, 13]))

    bubble_sort_obj = BubbleSortSolution()
    print("\nBubble sort:")
    print(bubble_sort_obj.bubbleSort([64, 34, 25, 12, 22, 11, 90]))

    insertion_sort_obj = InsertionSortSolution()
    print("\nInsertion sort:")
    print(insertion_sort_obj.insertionSort([12, 11, 13, 5, 6]))
