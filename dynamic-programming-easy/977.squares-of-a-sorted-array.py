#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    # 2 pointers, 頭尾都是從大到小往0走
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count = len(nums)
        ans = [0] * count
        left = 0
        right = count - 1
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        for i in range(count - 1, -1, -1):
            if left_square > right_square:
                ans[i] = left_square
                left += 1
                left_square = nums[left] ** 2
            else:
                ans[i] = right_square
                right -= 1
                right_square = nums[right] ** 2
        return ans

    
    # New sorted array
    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])
    
    # Built sort
    def sortedSquares_1(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        nums.sort()
        return nums
        
# @lc code=end

