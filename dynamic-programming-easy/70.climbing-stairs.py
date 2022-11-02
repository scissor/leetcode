#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # Fib: RecursionError: maximum recursion depth exceeded in comparison
    def climbStairs_1(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        
        return self.climbStairs(n) + self.climbStairs(n-1)
    
    # Self long solution
    def climbStairs(self, n: int) -> int:
        temp1 = 0
        temp2 = 1
        sum = 0
        for i in range(n):
            sum = temp1 + temp2
            temp1 = temp2
            temp2 = sum
            
        return sum
    
    # Elegant Swap
    def climbStairs_3(self, n:int) -> int:
        fst, snd = 0, 1
        
        for i in range(1, n+1):
            snd, fst = fst + snd, snd
        return snd
    
    # Fib by list
    # def __init__(self):
    #     self.fib = [0,1,2]
    #     for i in range(3,46):
    #         self.fib.append(self.fib[i-1] + self.fib[i-2]);
            
    def climbStairs_4(self, n: int) -> int:
        return self.fib[n]
    
    # Still not quick, why?
    def climbStairs_5(self, n: int) -> int:
        d = {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89, 11: 144, 12: 233, 13: 377, 14: 610, 15: 987, 16: 1597, 17: 2584, 18: 4181, 19: 6765, 20: 10946, 21: 17711, 22: 28657, 23: 46368, 24: 75025, 25: 121393, 26: 196418, 27: 317811, 28: 514229, 29: 832040, 30: 1346269, 31: 2178309, 32: 3524578, 33: 5702887, 34: 9227465, 35: 14930352, 36: 24157817, 37: 39088169, 38: 63245986, 39: 102334155, 40: 165580141, 41: 267914296, 42: 433494437, 43: 701408733, 44: 1134903170, 45: 1836311903}
        return d[n]
    
    # Top down + memorization (dictionary)  
    def __init__(self):
        self.dic = {1:1, 2:2}
        
    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
        
# @lc code=end

