#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        index = 0
        
        while l <= r:
            # index = math.floor((l + r) / 2)
            index = (l + r) // 2
            if nums[index] < target:
                l = index + 1
            elif nums[index] > target:
                r = index - 1
            else:
                return index
            
        return -1
# @lc code=end

