class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(day: int, is_holding: bool) -> int:
            if day >= len(prices):
                return 0
            max_profit = dp(day+1, is_holding)
            if is_holding:
                max_profit = max(max_profit, prices[day] - fee + dp(day+1, False))
            else:
                max_profit = max(max_profit, -prices[day] + dp(day+1, True))
            return max_profit
        
        return dp(0, False)

