class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                print(profit)
                max_profit = max_profit + profit

            l = l + 1
            r = r + 1

        return max_profit
