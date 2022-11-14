#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    # 用 zip 分割字串後，再用 set 判斷是否唯一
    # ('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')
    def longestCommonPrefix_4(self, strs: List[str]) -> str:
      prefix = ''
      for char_set in zip(*strs):
        if len(set(char_set)) > 1:
          break
        prefix += char_set[0]
      return prefix

    # Same to solution 2, but use sort
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1, s2 = strs[0], strs[-1]
        s1Len, s2Len = len(s1), len(s2)

        i = 0
        while i < s1Len and i < s2Len and s1[i] == s2[i]:
            i += 1
        return s1[:i]
    
    # 不是比較最短和最長的字串，而是字母差異最大的 flo v.s fli
    # 以 [flower, flow, flight] 來說，min = flight，max = flower
    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        s1, s2 = min(strs), max(strs)
        s1Len, s2Len = len(s1), len(s2)

        print(s1, s2)
        i = 0
        while i < s1Len and i < s2Len and s1[i] == s2[i]:
            i += 1
        return s1[:i]

    # Brute solution, slow (< 50%)
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        result = ""
        source = strs[0]
        srcLen = len(source)
        strLen = len(strs)

        for i in range(srcLen):
            for j in range(strLen):
                target = strs[j]
                c = source[i]

                if len(target) <= i or c != target[i]:
                    return result
            result += c
        return result
        
# @lc code=end

