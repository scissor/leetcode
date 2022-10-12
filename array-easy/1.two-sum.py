#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # Solution 1: O(n2)
    #     def twoSum(self, nums: List[int], target: int) -> List[int]:
    #         count = len(nums)
    #         for i in range(count):
    #             num = nums[i]

    #             for j in range(i + 1, count):
    #                 if (num + nums[j] == target):
    #                     return [i, j]
    #         return [0, 0]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if num in hash:
                return [hash[num], i]

            hash[complement] = i

        return [0, 0]


# @lc code=end
