#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        a = ""
        for i in s:
            if i in alpha:
                a += i
                
        return a[:] == a[::-1]
    
    # 2 pointers
    def isPalindrome_2(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
        
    def isPalindrome_1(self, s: str) -> bool:
        alphabets = ""
        for c in s:
            if c.isalnum():
                alphabets += c.lower()
        
        count = int(len(alphabets) / 2)
        
        for i in range(count):
            if alphabets[i] != alphabets[~i]:
                return False
            
        return True
        
# @lc code=end

