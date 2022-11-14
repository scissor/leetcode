#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Math magic
    def singleNumber(self, nums: List[int]) -> int:
	    return 2 * sum(list(set(nums))) - sum(nums)
    
    # XOR: Save variable memory 
    def singleNumber_3(self, nums: List[int]) -> int:
        for n in nums[1:]:
            nums[0] ^= n
        return nums[0]
    
    # XOR: X ^ 0 = X, X ^ X = 0
    def singleNumber_2(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = num ^ result
        return result
    
    # Brute solution with no addition space
    def singleNumber_1(self, nums: List[int]) -> int:
        length = len(nums)
        if length % 2 != 0:
            length -= 1
        
        nums.sort()
        for i in range(0, length, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]
        
# @lc code=end

