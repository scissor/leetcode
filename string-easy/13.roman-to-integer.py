#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    hash = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000
    }

    # Use pointer
    def romanToInt_4(self, s: str) -> int:
        i = sum = 0
        while i < len(s) - 1:
            d1 = self.hash[s[i]]
            d2 = self.hash[s[i + 1]]

            if d2 > d1:
                sum += d2 - d1
                i += 2
            else:
                sum += d1
                i += 1
        
        if i != len(s):
            sum += self.hash[s[-1]]
        return sum
    
    # Use bigger than to check, but slow
    def romanToInt_3(self, s: str) -> int:
        sum = 0
        prev = None
        for c in s:
            now = self.hash[c]
            sum += now

            if prev and now > prev:
                sum -= prev * 2
                prev = None

            prev = now

        return sum


    # Really cool answer
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        sum = 0
        for c in s:
            sum += self.hash[c]

        return sum


    # Self solution with hash
    def romanToInt_1(self, s: str) -> int:
        marks = {
            "I": ['V', 'X'], 
            "X": ['L', 'C'], 
            "C": ['D', 'M']
        }

        mark = None
        sum = 0
        for c in s:
            sum += self.hash[c]

            if mark and c in marks[mark]:
                sum -= self.hash[mark] * 2
                mark = None
            elif c in marks:
                mark = c
        return sum
        
# @lc code=end

