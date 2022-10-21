#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        stack = []
        
        for c in s:
            if c in hash:
                stack.append(c)
            else:
                if len(stack) > 0 and hash[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
# @lc code=end

