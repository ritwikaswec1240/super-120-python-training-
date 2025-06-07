#myPow – Power function
#Subsets – Generate all subsets
#check_subsequenceSum – Check if a subsequence adds up to a target
#generateParentheses – Generate valid parentheses
#Binary conversion – Convert decimal to binary

from typing import List

# 1. Power Function (x^n)
class PowerSolution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n
        return power(x, n)


# 2. Generate Subsets
class SubsetsSolution:
    def generate(self, ind, curr, ans, nums):
        if ind == len(nums):
            ans.append(curr.copy())
            return
        curr.append(nums[ind])
        self.generate(ind + 1, curr, ans, nums)
        curr.pop()
        self.generate(ind + 1, curr, ans, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.generate(0, [], ans, nums)
        return ans


# 3. Check Subsequence Sum Equals Target
class SubsequenceSumSolution:
    def check(self, ind, arr, k):
        if k == 0:
            return True
        if k < 0 or ind == len(arr):
            return False
        if self.check(ind + 1, arr, k - arr[ind]):
            return True
        return self.check(ind + 1, arr, k)

    def check_subsequenceSum(self, arr: List[int], k: int) -> bool:
        return self.check(0, arr, k)


# 4. Generate Valid Parentheses
class ParenthesesSolution:
    def generateParentheses(self, n: int) -> List[str]:
        def generate(open_count, close_count, curr_str, ans):
            if open_count == n and close_count == n:
                ans.append(curr_str)
                return
            if open_count < n:
                generate(open_count + 1, close_count, curr_str + "(", ans)
            if close_count < open_count:
                generate(open_count, close_count + 1, curr_str + ")", ans)

        ans = []
        generate(0, 0, "", ans)
        return ans


# 5. Binary Conversion
def decimal_to_binary(a: int) -> str:
    if a == 0:
        return "0"
    rem = ""
    while a:
        rem = str(a % 2) + rem
        a = a // 2
    return rem


# ---------- Example Usage ----------
if __name__ == "__main__":
    # 1. Power
    power_obj = PowerSolution()
    print("Power(2, 10):", power_obj.myPow(2, 10))  # Output: 1024.0

    # 2. Subsets
    subset_obj = SubsetsSolution()
    print("Subsets of [1,2,3]:", subset_obj.subsets([1, 2, 3]))

    # 3. Check Subsequence Sum
    sub_sum_obj = SubsequenceSumSolution()
    print("Check Subsequence Sum:", sub_sum_obj.check_subsequenceSum([1, 2, 3, 4], 6))  # Output: True

    # 4. Generate Parentheses
    par_obj = ParenthesesSolution()
    print("Generate Parentheses (n=3):", par_obj.generateParentheses(3))

    # 5. Binary Conversion
    print("Binary of 8:", decimal_to_binary(8))  # Output: 1000
