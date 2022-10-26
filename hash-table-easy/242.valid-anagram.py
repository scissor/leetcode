#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        chars = [0] * 26
        for i in range(len(s)):
            chars[ord(s[i]) - 97] += 1
            chars[ord(t[i]) - 97] -= 1
            
        for c in chars:
            if c != 0:
                return False
            
        return True
    
    def isAnagram_4(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram_3(self, s, t):
        return sorted(s) == sorted(t)
    
    # 1 Hash
    def isAnagram_2(self, s: str, t: str) -> bool:
        hash = {}
        
        for c in s:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        
        for c in t:
            if c in hash:
                hash[c] -= 1
            else:
                return False
                
        for c in hash:
            if hash[c] != 0:
                return False
            
        return True
    
    # 2 Hash
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash = {}
        hash2 = {}
        
        for c in s:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        
        for c in t:
            if c in hash2:
                hash2[c] += 1
            else:
                hash2[c] = 1
                
        for c in hash:
            if c not in hash2 or hash[c] != hash2[c]:
                return False
            
        return True
        
# @lc code=end

