# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         min_val = min(prices)
#         n = len(prices)
#         if min_val == prices[-1]:
#             return 0
#         else:
#             index_of_min = prices.index(min_val)
#             max_val = prices[index_of_min]
#             for i in range(index_of_min, n):
#                 if prices[i]>max_val:
#                     max_val = prices[i]
#             return max_val - min_val

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_val = float('inf')  # Initialize to a very large number
        max_profit = 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_val:
                min_val = price
            # Calculate the current profit and update the maximum profit
            current_profit = price - min_val
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit
