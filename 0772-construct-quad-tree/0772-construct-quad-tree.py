"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def dfs(row, col, n):
            cond = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        cond = False
                        break
            
            if cond:
                return Node(grid[row][col], True)
            n //= 2
            tl = dfs(row, col, n)
            tr = dfs(row, col + n, n)
            bl = dfs(row + n, col, n)
            br = dfs(row + n, col + n, n)

            return Node(grid[row][col], False, tl, tr, bl, br)
        
        return dfs(0, 0, n)