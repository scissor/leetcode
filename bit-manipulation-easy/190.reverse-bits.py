#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # String
    def reverseBits_2(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
    
    # Bit operation
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
        
# @lc code=end

