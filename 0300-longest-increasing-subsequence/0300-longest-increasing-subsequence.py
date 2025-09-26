class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:  
        dp = {0:1}
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            max_len = 1
            for j in range(0, i):
                if nums[j] < curr:
                    max_len = max(max_len, dp[j] + 1)
            dp[i] = max_len
        print(dp)
        return max(dp.values())
        
