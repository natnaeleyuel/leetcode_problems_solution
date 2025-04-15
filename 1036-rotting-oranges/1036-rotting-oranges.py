class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def ib(n, m, x, y): return x < n  and x >= 0 and y >= 0 and y < m 
        def dr(): return [(1, 0), (0, 1), (0, -1), (-1, 0)]
        n = len(grid)
        m = len(grid[0])
        queue = deque([])
        count = 0
        time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        direction = dr()
        while queue and count > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for row, col in direction:
                    new_row = i + row
                    new_col = j + col
                    if ib(n, m, new_row, new_col) and grid[new_row][new_col] == 1:
                        count -= 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            time += 1
        
        return -1 if count else time