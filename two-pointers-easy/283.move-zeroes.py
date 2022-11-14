#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        length = len(nums)
        
        for i in range(length):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        
# @lc code=end

