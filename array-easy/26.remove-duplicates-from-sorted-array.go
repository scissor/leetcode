/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	index := 0
	length := len(nums)

	for i := 0; i < length; i++ {
		if nums[i] == nums[index] {
			continue
		}

		index++
		nums[index] = nums[i]
	}

	return index + 1
}

// @lc code=end

