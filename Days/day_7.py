# Stock Buy and Sell – Max one Transaction Allowed


class Solution:
    def maximumProfit(self, prices):
        # code here
        
     
        max_profit=0
        min_int=float('inf')
        
        for i in prices:
            min_int=min(min_int,i)
            max_profit=max(max_profit,i-min_int)
        return max_profit
                
