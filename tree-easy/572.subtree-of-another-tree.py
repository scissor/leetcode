#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Convert to string
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def convert(p):
            return "^" + str(p.val) + convert(p.left) + convert(p.right) if p else "$"
        return convert(subRoot) in convert(root)


    # Recursive
    def isSubtree_1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(left, right): 
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and isSame(left.left, right.left) and isSame(left.right, right.right)

        if not root: return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
# @lc code=end

