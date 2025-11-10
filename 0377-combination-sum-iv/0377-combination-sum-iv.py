class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}
        for tot in range(1, target + 1):
            dp[tot] = 0
            for n in nums:
                dp[tot] += dp.get(tot - n, 0)

        return dp[target]