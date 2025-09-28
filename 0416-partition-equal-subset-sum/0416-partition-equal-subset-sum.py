class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        target, mod = divmod(sum(nums), 2)
        n = len(nums)
        dp = [False] * (target+1)
        dp[0] = True
        if mod != 0:
            return False
        if target in nums:
            return True
        if max(nums) > target:
            return False
        for i in range(n):
            curr = nums[i]
            for j in range(target, curr-1, -1):
                dp[j] = dp[j] or dp[j-curr]
            if dp[target]:
                return True
        return dp[target]
