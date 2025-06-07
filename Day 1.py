# Day 1 - Python Practice

# Vowels
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)


# String Number (incomplete logic - preserved as-is)
def stringnum(s):
    res = ""
    i = 0
    while i < len(s):
        nums = ""
        # Logic missing, placeholder retained
        i += 1


# Unique value in the list
my_list = [1, 1, 2, 2, 3]
unique_value = []
for item in my_list:
    if my_list.count(item) == 1:
        unique_value.append(item)
print("Unique value in the list:", unique_value)


# Make each alphabet come with numbers - Sum of the index in a string
string = input("Enter a string: ")
index_sum = 0
for index in range(len(string)):
    index_sum += index
print("Sum of indices in the string:", index_sum)


# Check if one string is a rotation of another (commented logic)
# s = input()
# substr = input()
# if len(substr) <= len(s):
#     if substr in (s + s):
#         print("True")
#     else:
#         print("False")


# Prime numbers between 1 and 100
print("Prime numbers between 1 and 100 are:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


# Method 1 - Interleave two strings
string1 = "abcd"
string2 = "jk"

min_len = min(len(string1), len(string2))
result = ""
for i in range(min_len):
    result += string1[i] + string2[i]

result += string1[min_len:] + string2[min_len:]
print(result)


# Method 2 - Interleave with case change (has bugs in original logic, preserved as-is)
string1 = "abcd"
string2 = "jk"
i = 0
res = ""
while i < len(string1) and i < len(string2):
    res += string1[i] + string2[i]
    i += 1
while i < len(string1):
    res += chr(ord(string2[i]) - 32)  # May cause IndexError, original logic kept
    i += 1
while i < len(string2):
    res += chr(ord(string2[i]) - 32)
    i += 1


# Circular String
class CircularString:
    def __init__(self, s):
        self.s = s

    def rotate(self, n):
        n = n % len(self.s)
        return self.s[n:] + self.s[:n]

    def get_substring(self, start, length):
        start = start % len(self.s)
        return self.s[start:start + length] + self.s[:max(0, start + length - len(self.s))]

    def __str__(self):
        return self.s
