class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n : 1}

        def dfs(idx):
            if idx in dp:
                return dp[idx]
            if s[idx] == "0":
                return 0

            res = dfs(idx + 1)
            if (idx + 1 < n and (s[idx] == "1" or s[idx] == "2" and s[idx + 1] in "0123456")):
                res += dfs(idx + 2)
            dp[idx] = res
            return res
        
        return dfs(0)
