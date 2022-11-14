#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits_4(self, n: int) -> List[int]:
        if n == 0: return [0]
        
        ret = [0, 1]
        for i in range(2, n, 2):
            val = ret[i >> 1]
            ret.append(val)
            ret.append(val + 1)
        if not n % 2:
            ret.append(ret[n >> 1])
        return ret
    
    # 乘以 2 只是添加一個零
    # 任何數字的位數都將與該數字的一半相同，如果它是奇數，則額外增加一個
    def countBits_3(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter

        
    # 1 list extend
    def countBits_2(self, n: int) -> List[int]:
        bits = [0]
        while len(bits) < n+1:
            bits.extend([b + 1 for b in bits])
        return bits[:n+1]
    
    # # Brute solution by list concat
    def countBits(self, n: int) -> List[int]:
        subset = [1]
        bits = [0, 1]

        while len(bits) < n+1:
            subset += [b + 1 for b in subset]
            bits += subset
        
        return bits[:n+1]
        
# @lc code=end

