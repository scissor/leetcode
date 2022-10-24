#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        profits = [0]
        
        for price in prices:
            if price > max_price:
                max_price = price
                profits.append(max_price - min_price)
                
            if price < min_price:
                min_price = price
                max_price = min_price

        return max(profits)
    
    # Kadane's Algorithm
    def maxProfit_3(self, prices: List[int]) -> int:
        distance = 0
        max_distance = 0
        
        for i in range(1, len(prices)):
            distance += prices[i] - prices[i-1]
            distance = max(0, distance)
            max_distance = max(max_distance, distance)
            
        return max_distance

    
    def maxProfit_2(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit
    
    
    def maxProfit_1(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            if price[left] < price[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
                
            right += 1
            
        return max_profit
        
# @lc code=end

