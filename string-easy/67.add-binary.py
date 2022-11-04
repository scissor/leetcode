#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = sum = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            sum = d1 + d2 + carry
            carry = 1 if sum > 1 else 0
            result = str(int(sum % 2)) + result
            i, j = i-1, j-1 

        return result
    
    # Python Binary Add
    def addBinary_2(self, a: str, b: str) -> str:
        s = int(a,2) + int(b,2)
        s = bin(s)
        return s[2:]

    # Self long & slow solution (41%)
    def addBinary_1(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        l = min(len_a, len_b)
        carry = 0
        sum = 0
        result = ""

        for i in range(l):
            sum = int(a[~i]) + int(b[~i]) + carry
            if sum > 1:
                carry = 1
            else:
                carry = 0

            result = str(int(sum % 2)) + result

        if len_a == len_b:
            if carry > 0:
                return "1" + result
            
            return result

        target = a if len_a > len_b else b
        for i in range(len(target) - l):
            sum = int(target[~(l + i)]) + carry
            if sum > 1:
                carry = 1
            else:
                carry = 0

            result = str(int(sum % 2)) + result

        if carry > 0:
            return "1" + result

        return result
        
# @lc code=end

