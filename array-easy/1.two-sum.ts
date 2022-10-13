/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
    var hash = {};
    for (var i = 0; i < nums.length; i++) {
        var num = nums[i];
        var complement = target - num;

        if (hash[num] !== undefined) {
            return [hash[num], i];
        }

        hash[complement] = i
    }

    return [];
};
// @lc code=end

