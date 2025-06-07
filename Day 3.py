# Day 3 - Python Practice

# 1. Expand compressed string (e.g., "3a4b6c")
str1 = "3a4b6c"
res = ""
for i in range(0, len(str1), 2):
    res += int(str1[i]) * str1[i + 1]
print("Expanded string 1:", res)

# 2. Variable-length numbers before characters
str2 = "31a4b111c"
res = ""
num = ""
for i in str2:
    if i.isdigit():
        num += i
    else:
        res += int(num) * i
        num = ""
print("Expanded string 2:", res)

# 3. String with multiple letters after number (e.g., "31abc1h")
str3 = "31abc1h"
res = ""
num = ""
alp = ""
i = 0
while i < len(str3):
    while i < len(str3) and str3[i].isdigit():
        num += str3[i]
        i += 1
    while i < len(str3) and str3[i].isalpha():
        alp += str3[i]
        i += 1
    res += int(num) * alp
    num = ""
    alp = ""
print("Expanded string 3:", res)

# 4. Binary conversion
a = 8
rem = ""
while a:
    rem += str(a % 2)
    a = a // 2
print("Binary of 8:", rem[::-1])

# 5. Binary to Decimal
a = "101"
a = a[::-1]
dec = 0
for i in range(len(a)):
    dec += int(a[i]) * (2 ** i)
print("Decimal of 101:", dec)

# 6. Count bits
a = 8
count = 0
while a:
    a = a >> 1
    count += 1
print("Number of bits:", count)

# 7. Count set bits
a = 8
count = 0
while a:
    if a & 1 == 1:
        count += 1
    a = a >> 1
print("Set bits count:", count)

# 8. Count number of trailing zeros
a = 16
count = 0
while a & 1 == 0:
    a = a >> 1
    count += 1
print("Trailing zeros:", count)

# 9. Count reset bits (i.e., 0s among total bits)
a = 8
count = 0
temp = a
bits = 0
while temp:
    temp = temp >> 1
    bits += 1

temp = a
while temp:
    if temp & 1:
        count += 1
    temp = temp >> 1

reset_bits = bits - count
print("Reset bits:", reset_bits)

# 10. Position of the only set bit in a power of two
a = 16
count = 0
temp = a
while a:
    a = a >> 1
    count += 1
while temp & 1 == 0:
    temp = temp >> 1
    count -= 1
print("Position of the only set bit:", count)

# 11. Clearing the ith bit of a number
def clear_ith_bit(a, i):
    mask = ~(1 << i)
    return a & mask

print("Clearing 0th bit of 5:", clear_ith_bit(5, 0))

# 12. Set ith Bit using Bitwise OR
def set_ith_bit(a, i):
    mask = 1 << i
    return a | mask

print("Setting 2nd bit of 8:", set_ith_bit(8, 2))

# 13. Check if ith bit is set
def is_ith_bit_set(a, i):
    mask = 1 << i
    return 1 if mask & a else 0

print("Is 3rd bit set in 8?", is_ith_bit_set(8, 3))

# 14. Check if number is power of 2
def is_power_of_two(a):
    return a & (a - 1) == 0 and a != 0

print("Is 6 power of 2?", is_power_of_two(6))

# 15. Find unique number using XOR
a = [3, 4, 3, 4, 9]
res = 0
for i in a:
    res ^= i
print("Unique number:", res)
