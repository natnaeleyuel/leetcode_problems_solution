class DisjointUnion:
    def __init__(self, rows, cols):
        self.root = {}
        for i in range(-1, rows * 2):
            for j in range(-1, cols * 2):
                self.root[(i, j)] = (i, j)
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y

class Solution:
    def hasValidPath(self, grid):
        if not grid or not grid[0]:
            return False
        
        m, n = len(grid), len(grid[0])
        dsu = DisjointUnion(m, n)
        
        connection_rules = {
            1: [(0, -1), (0, 1)],   
            2: [(-1, 0), (1, 0)],  
            3: [(0, -1), (1, 0)],   
            4: [(0, 1), (1, 0)],  
            5: [(-1, 0), (0, -1)], 
            6: [(-1, 0), (0, 1)]   
        }
        
        for i in range(m):
            for j in range(n):
                cell_type = grid[i][j]
                for di, dj in connection_rules[cell_type]:
                    dsu.merge((i * 2, j * 2), (i * 2 + di, j * 2 + dj))
        
        start = (0, 0)
        end = (m * 2 - 2, n * 2 - 2)
        return dsu.find(start) == dsu.find(end)