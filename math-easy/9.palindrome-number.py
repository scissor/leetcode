#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    # Revert string
    def isPalindrome_3(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    # Official Solution: Revert number
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False

        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x = x // 10
        
        return x == revert or x == revert // 10

    # int => string (91%)
    def isPalindrome_1(self, x: int) -> bool:
        if x < 0: return False

        s = str(x)
        l = int(len(s) * 0.5)

        for i in range(l):
            if s[i] != s[~i]:
                return False

        return True
        
# @lc code=end

