#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    # 與自身少 1 的數做 and，每次會少一個 1
    # 更快：省下右移的時間，只有 And
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans

    # Bit operation (And + 右移)
    def hammingWeight_2(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count

    # Brute solution
    def hammingWeight_1(self, n: int) -> int:
        count = 0
        while n:
            if n % 2:
                count += 1
            n >>= 1
        return count
        
# @lc code=end

