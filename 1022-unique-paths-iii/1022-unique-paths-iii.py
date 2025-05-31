class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def inbound(x, y, n, m):
            return 0 <= x < m and 0 <= y < n
        
        def dr():
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        n = len(grid)
        m = len(grid[0])
        count_empty_squares = 0 
        start = None

        for i in range(n):
            for j in range(m):
                count_empty_squares += grid[i][j] == 0
                if not start and grid[i][j] == 1:
                    start = (i, j)
        
        directions = dr()
        def backtrack(row, col):
            nonlocal count_empty_squares
            result = 0
            for r, c in directions:
                x = col + c
                y = row + r
                if inbound(x, y, n, m):

                    if grid[y][x] == 0:

                        count_empty_squares -= 1
                        grid[y][x] = -1
                        result += backtrack(y, x)

                        count_empty_squares += 1
                        grid[y][x] = 0


                    elif grid[y][x] == 2:
                        result += count_empty_squares == 0

            return result
        
        return backtrack(start[0], start[1])

        


        
        
        
