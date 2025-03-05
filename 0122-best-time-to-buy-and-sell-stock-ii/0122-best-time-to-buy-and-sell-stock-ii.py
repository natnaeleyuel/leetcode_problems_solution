class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0]
        res = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                res += diff

        return res


