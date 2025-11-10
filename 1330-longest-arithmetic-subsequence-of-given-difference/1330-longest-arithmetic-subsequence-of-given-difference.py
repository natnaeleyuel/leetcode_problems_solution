class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
        
        return max(dp.values())
