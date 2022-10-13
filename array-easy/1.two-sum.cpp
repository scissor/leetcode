/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    map<int, int> hash = {};

    for (int i = 0; i < nums.size(); i++) {
      int num = nums[i];
      int complement = target - num;

      if (hash.find(num) != hash.end())
        return vector<int>{i, hash[num]};
      else
        hash.insert({complement, i});
    }

    return vector<int>{};
  }
};
// @lc code=end
