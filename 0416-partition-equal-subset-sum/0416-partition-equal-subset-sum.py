class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        l = s // 2
        if s % 2 != 0:
            return False
        dp = [True] + [False] * l
        for x in nums:
            for i in range(l, x - 1, -1): 
                dp[i] |= dp[i - x]

            if dp[l]: return True
        return dp[l]
        
