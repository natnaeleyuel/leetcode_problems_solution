class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        
        def dfs(ind, m, n):
            if ind == len(strs):
                return 0
            if (ind, m, n) in dp:
                return dp[(ind, m, n)]
            
            count_m = strs[ind].count("0")
            count_n = strs[ind].count("1")
            dp[(ind, m, n)] = dfs(ind + 1, m, n)
            if count_m <= m and count_n <= n:
                dp[(ind, m, n)] = max(
                    dp[(ind, m, n)], 
                    1 + dfs(ind + 1, m - count_m, n - count_n)
                )
            
            return dp[(ind, m, n)]
        
        return dfs(0, m, n)