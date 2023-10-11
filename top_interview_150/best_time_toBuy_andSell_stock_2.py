from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0
        elif prices == sorted(prices, reverse=True):
            print('sorted')
            return 0
        else:
            max_profit = 0
            min_price = prices[0]
            for i in range(1, len(prices)):
                print('\ni: ', i)
                if prices[i] < min_price: 
                    min_price = prices[i]
                    print('min_price: ', min_price)
                elif prices[i] - min_price > 0:
                    max_profit += prices[i] - min_price
                    min_price = prices[i]
                    print('max_profit: ', max_profit)
                    print('min_price: ', min_price)
            return max_profit

        
    
if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
    # prices = [1,2,3,4,5]
    # print(sol.maxProfit(prices))
    # prices = [7,6,4,3,1]
    # print(sol.maxProfit(prices))
    
