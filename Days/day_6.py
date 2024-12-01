# Stock Buy and Sell – Multiple Transaction Allowed

from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        total_profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                total_profit+=(prices[i]-prices[i-1])
        return total_profit
