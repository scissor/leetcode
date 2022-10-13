/*
 * @lc app=leetcode id=26 lang=typescript
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
  var index = 0;
  var len = nums.length;

  for (var i = 0; i < len; i++) {
    if (nums[i] == nums[index]) {
      continue;
    }

    index++;
    nums[index] = nums[i];
  }

  return index + 1;
}
// @lc code=end
