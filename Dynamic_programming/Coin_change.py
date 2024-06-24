# Time complexity of the dp solution is O(len(coins)*amount) whereas the time complexity of the recursion solution
# is O(len(coins)^amount)

# Dynamic programming solution
class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return dp[amount] if dp[amount] != float('inf') else -1


# Recursive solution
def coinChange_recursive(coins: 'List[int]', amount: int) -> int:
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    min_coins = float('inf')
    for coin in coins:
        res = coinChange_recursive(coins, amount - coin)
        if res >= 0 and res < min_coins:
            min_coins = 1 + res

    return min_coins if min_coins != float('inf') else -1
