class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        Approach to solve
        min_price variable keep track of minimum price
        max_profit keep track of max profit

        at every point we find min price we alo find profit, and compare to maximum profit, and at last max profit 
        is returned
        """
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price
            
            # finding profit
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
