#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def height(p):
            if not p: return 0       
            left, right = height(p.left), height(p.right)
            self.ans = max(self.ans, left + right)   
            return 1 + max(left, right)
            
        height(root)
        return self.ans
        
# @lc code=end

