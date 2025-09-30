class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < abs(target) or (sum(nums) - target) % 2 == 1:
            return 0
        
        m = (sum(nums) - target) // 2
        n = len(nums)

        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(m+1):
                dp[i][j] += dp[i-1][j]
                if j >= curr:
                    dp[i][j] += dp[i-1][j-curr]
        
        return dp[-1][-1]