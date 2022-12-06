#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # 排序後掃負數，利用 set 確認補數，再配合 tuple 確認唯一
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            # Avoid [0,0,0]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            x = nums[i]
            if x > 0:
                break

            s = set()
            for y in nums[i+1:]:
                if -x-y in s:
                    result.add(tuple([x, -x-y, y]))
                s.add(y)
        return [i for i in result]
# @lc code=end

