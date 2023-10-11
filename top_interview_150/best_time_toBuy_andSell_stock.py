from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price: 
                min_price = prices[i]
            elif prices[i] - min_price > max_profit: 
                max_profit = prices[i] - min_price
        return max_profit
    
if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices))
    prices = [2,4,1]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))
