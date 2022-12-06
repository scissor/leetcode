#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        min_diff = abs(ans - target)

        for i in range(len(nums) - 2):
            l, r = i+1, len(nums)-1
            sub_target = target - nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == sub_target: 
                    return target

                diff = abs(s - sub_target)
                if diff < min_diff:
                    min_diff = diff
                    ans = s + nums[i]

                if s < sub_target:
                    l += 1
                elif s > sub_target:
                    r -= 1
        return ans
                
    # Brute Solution: Time Limit Exceeded
    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = ans = 1000000

        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    diff = abs(s - target)
                    
                    if diff == 0:
                        return target

                    if diff < min_diff:
                        min_diff = diff
                        ans = s
        return ans
        
# @lc code=end

