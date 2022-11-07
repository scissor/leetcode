#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    # Set
    def containsDuplicate_3(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            hset.add(idx)
        return False
    
    # Set Length
    def containsDuplicate(self, nums: List[int]) -> bool:
	    return len(set(nums)) != len(nums)

    # Dictionary
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                return True
            hash[num] = 0
        return False
        
# @lc code=end

