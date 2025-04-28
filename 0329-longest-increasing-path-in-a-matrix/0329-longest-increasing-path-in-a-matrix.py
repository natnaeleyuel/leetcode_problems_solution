class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        def dr(): return [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def ib(n, m, x, y): return x >= 0 and x < n and y >= 0 and y < m
        
        n = len(matrix)
        m = len(matrix[0])
        directions = dr()
        
        graph = defaultdict(list)
        in_degree = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ib(n, m, ni, nj) and matrix[ni][nj] > matrix[i][j]:
                        graph[(i, j)].append((ni, nj))
                        in_degree[ni][nj] += 1
        
        queue = deque()
        comp = [[1 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if in_degree[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            for ni, nj in graph[(i, j)]:
                if comp[ni][nj] < comp[i][j] + 1:
                    comp[ni][nj] = comp[i][j] + 1
                in_degree[ni][nj] -= 1
                if in_degree[ni][nj] == 0:
                    queue.append((ni, nj))
        
        return max(max(row) for row in comp)