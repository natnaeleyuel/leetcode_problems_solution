class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        res[n][m - 1] = 0
        for i in range(n - 1, - 1, - 1):
            for j in range(m - 1, - 1, - 1):
                res[i][j] = grid[i][j] + min(res[i + 1][j], res[i][j + 1])
        
        return res[0][0]