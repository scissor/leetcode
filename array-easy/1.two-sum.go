/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	hash := map[int]int{}
	length := len(nums)

	for i := 0; i < length; i++ {
		num := nums[i]
		complement := target - num

		if val, ok := hash[num]; ok {
			return []int{val, i}
		}

		hash[complement] = i
	}

	return []int{}
}

// @lc code=end

