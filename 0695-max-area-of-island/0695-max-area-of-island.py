class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        inbound = lambda x, y: x >= 0 and x < n and y >= 0 and y < m
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            res = 1
            for r, c in direction:
                new_row = row + r 
                new_col = col + c
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    res += dfs(new_row, new_col)
            return res
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area

