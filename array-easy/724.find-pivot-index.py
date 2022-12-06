#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums) - nums[0]
        
        if l == r: return 0
        
        l += nums[0]
        
        for i in range(1, len(nums)):
            r -= nums[i]
            if l == r: return i
            l += nums[i]
            
        return -1
            
# @lc code=end

