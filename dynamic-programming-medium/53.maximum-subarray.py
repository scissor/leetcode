#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    # Divide & Conquer (分成左中右)
    def maxSubArray_4(self, nums):
        def maxSubArray(nums, l, r):
            if l > r: return -inf

            mid = (l + r) // 2
            l_sum, r_sum, temp = 0, 0, 0

            for i in range(mid-1, l-1, -1):
                l_sum = max(l_sum, temp := temp + nums[i])

            temp = 0
            for i in range(mid+1, r+1):
                r_sum = max(r_sum, temp := temp + nums[i])

            return max(
                maxSubArray(nums, l, mid-1), 
                maxSubArray(nums, mid+1, r), 
                l_sum + nums[mid] + r_sum)
                
        return maxSubArray(nums, 0, len(nums)-1)
    
    # DP2
    def maxSubArray_3(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

    # DP: dp[i] = nums[i] + max(dp[i - 1], 0)]
    # [-2,1,-3,4,-1,2,1,-5,4] =>
    # [-2,-1,-3,4,3,5,6,1,5]
    def maxSubArray(self, nums: List[int]) -> int:
        temp = ans = nums[0]
        for i in range(1, len(nums)):
            temp = nums[i] + max(temp, 0)
            ans = max(temp, ans)
        return ans
    
    # Brute solution: Time Limit Exceeded O(n*n)
    def maxSubArray_1(self, nums: List[int]) -> int:
        ans = -inf
        temp = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                ans = max(ans, temp)
        return ans
        
# @lc code=end

