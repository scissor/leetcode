#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    # Moore's majority vote algorithm
    # https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        vote = nums[0]

        for num in nums:
            if count == 0:
                vote = num
                count = 1
            else:
                if num == vote:
                    count += 1
                else:
                    count -= 1

        return vote
        
    # Use unique list, but still slow (41%)
    def majorityElement_3(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        y = 0
        main = 0    
        for x in uniqueNums:
            count = nums.count(x)
            if count > y:
                y = count
                main = x
        return main
    
    # Sorted (55%)
    def majorityElement_2(self, nums: List[int]) -> int:
        return sorted(nums)[(int)(len(nums)/2)]
    
    # # Brute solution but slow (10.89%)
    def majorityElement_1(self, nums: List[int]) -> int:
        import math
        
        count = len(nums)
        if count < 3: return nums[0]
        
        hash = {}
        halfCount = math.ceil(count * 0.5)
        
        for i in range(count):
            num = nums[i]
            if num in hash:
                hash[num] += 1
                if hash[num] >= halfCount:
                    return num
            else:
                hash[num] = 1

        return 0
        
# @lc code=end

