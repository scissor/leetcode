/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        var len = nums.Length;

        // Solution 1: O(n2), O(1)
        /*
        for (var i = 0; i < len - 1; i++) {
            for (var j = i + 1; j < len; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[2] {i, j};
                }
            }
        }
        
        return null;
        */

        // Solution 2: O(n), O(n)
        var hash = new Dictionary<int, int>();
        var num = 0;
        for (var i = 0; i < len; i++)
        {
            num = nums[i];
            var complement = target - num;
            if (hash.ContainsKey(complement))
            {
                return new int[] { hash[complement], i };
            }

            if (!hash.ContainsKey(num))
            {
                hash.Add(nums[i], i);
            }
        }

        return null;
    }
}
// @lc code=end

