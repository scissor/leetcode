/*
 * @lc app=leetcode id=26 lang=csharp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        var index = 0;
        var len = nums.Length;
        for (var i = 0; i < len; i++)
        {
            if (nums[i] == nums[index])
            {
                continue;
            }

            index++;
            nums[index] = nums[i];
        }

        return index + 1;
    }
}
// @lc code=end

