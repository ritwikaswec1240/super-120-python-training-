# Day 2 - Python Practice

# 1. Moving zeros to the end (Method 1)
def move_zeros_to_end(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros

arr = [3, 0, 5, 6, 0, 7, 4]
result = move_zeros_to_end(arr)
print("After moving zeros to the end (method 1):", result)


# Method 2 (original logic, fixed syntax)
n = [3, 0, 5, 6, 0, 7, 4]
a = n.copy()
for i in a[:]:
    if i != 0:
        continue
    a.remove(0)
    a.append(0)
print("After moving zeros to the end (method 2):", a)


# 2. Finding the missing number
def finding_the_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number

numbers = [1, 2, 3, 5]
missing = finding_the_missing_number(numbers)
print("The missing number is:", missing)


# 3. Move even numbers to the end (Method 1)
def move_evens_to_end(arr):
    odds = [num for num in arr if num % 2 != 0]
    evens = [num for num in arr if num % 2 == 0]
    return odds + evens

arr = [1, 3, 5, 6, 4, 8]
results = move_evens_to_end(arr)
print("After moving even numbers to the end (method 1):", results)


# Method 2
a = [1, 3, 5, 6, 4, 8]
for i in a[:]:
    if i % 2 == 0:
        a.remove(i)
        a.insert(0, i)
a.reverse()
print("After moving even numbers to the end (method 2):", a)


# Method 3
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 0
i = 0
while i < len(l):
    if l[i] % 2 != 0:
        temp = l.pop(i)
        l.insert(k, temp)
        k += 1
        i = k
    else:
        i += 1

print("After moving even numbers to the end (method 3):", l)
