class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float('inf')] * n for _ in range(n)]

        def solve(i, j):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            down = triangle[i][j] + solve(i + 1, j)
            diag = triangle[i][j] + solve(i + 1, j + 1)
            dp[i][j] = min(down, diag)
            return dp[i][j]

        return solve(0, 0)    