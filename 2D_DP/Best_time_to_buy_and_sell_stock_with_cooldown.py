class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key = (i,buying) val = max_profit

        def dfs(i, Buying):
            if i >= len(prices):
                return 0

            if (i, Buying) in dp:
                return dp[(i, Buying)]

            if Buying:
                buy = dfs(i + 1, not Buying) - prices[i]
                cooldown = dfs(i + 1, Buying)
                dp[(i, Buying)] = max(buy, cooldown)

            else:
                sell = dfs(i + 2, not Buying) + prices[i]
                cooldown = dfs(i + 1, Buying)
                dp[(i, Buying)] = max(cooldown, sell)

            return dp[(i, Buying)]

        return dfs(0, True)


