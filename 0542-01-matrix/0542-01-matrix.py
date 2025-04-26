class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def dr(): return [(1, 0), (0, 1), (0, - 1), (-1, 0)]

        def ib(n, m, x, y): return x < n and x >= 0 and y >= 0 and y < m 

        n = len(mat)
        m = len(mat[0])
        mv = n * m
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = mv
        
        directions = dr()
        while queue:
            row, col = queue.popleft()
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if ib(n, m, new_row, new_col) and mat[new_row][new_col] > mat[row][col] + 1:
                    queue.append((new_row, new_col))
                    mat[new_row][new_col] = mat[row][col] + 1
         
        return mat