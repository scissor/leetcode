/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    int index = 0;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] == nums[index]) {
        continue;
      }

      index++;
      nums[index] = nums[i];
    }

    return index + 1;
  }
};
// @lc code=end
