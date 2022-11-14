#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        return int((count + 1) * count * 0.5) - sum(nums)
    
    def missingNumber_1(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return i + 1
        
# @lc code=end

