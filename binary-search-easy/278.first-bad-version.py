#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 0
        index = 0
        
        while left < right - 1:
            index = int((right - left) * 0.5)
            if isBadVersion(index):
                right = index
            else:
                left = index
                
            print(index, left, right)
                
        return right
# @lc code=end

