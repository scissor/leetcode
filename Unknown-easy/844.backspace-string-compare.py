#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    # String slice
    def backspaceCompare_3(self, s: str, t: str) -> bool:
        def transfer(s):
            result = ''
            for i in s:
                if i == "#":
                    result = result[:-1]
                else:
                    result += i
            return result
            
        return transfer(s) == transfer(t)
    
    # Use stack
    def backspaceCompare_2(self, s: str, t: str) -> bool:
        def transfer(s):
            chars = []
            for i in range(len(s)):
                if s[i] == '#':
                    if chars:
                        chars.pop()
                else:
                    chars.append(s[i])
            return chars
            
        return transfer(s) == transfer(t)


    # # Brute solution, use counter
    def backspaceCompare(self, s: str, t: str) -> bool:
        def transfer(s):
            s1 = ''
            markCount = 0
            i = 1
            while i <= len(s):
                if s[-i] == '#':
                    i += 1
                    markCount += 1
                else:
                    if markCount > 0:
                        i += 1
                        markCount -= 1
                    else:
                        s1 += s[-i]
                        i += 1
            return s1

        return transfer(s) == transfer(t)
        
# @lc code=end

