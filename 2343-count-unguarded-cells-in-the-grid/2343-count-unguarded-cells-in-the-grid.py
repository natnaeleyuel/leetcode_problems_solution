class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(len(guards)):
            r = guards[i][0]
            c = guards[i][1]
            grid[r][c] = 1

        for j in range(len(walls)):
            r = walls[j][0]
            c = walls[j][1]
            grid[r][c] = -1

        for r in range(m):
            guard_see = False
            for c in range(n):
                if grid[r][c] == 1:
                    guard_see = True
                elif grid[r][c] == -1:
                    guard_see = False
                elif guard_see:
                    grid[r][c] = 2
        
        for r in range(m-1, -1, -1):
            guard_see = False
            for c in range(n-1, -1, -1):
                if grid[r][c] == 1:
                    guard_see = True
                elif grid[r][c] == -1:
                    guard_see = False
                elif guard_see:
                    grid[r][c] = 2
        
        for c in range(n):
            guard_see = False
            for r in range(m):
                if grid[r][c] == 1:
                    guard_see = True
                elif grid[r][c] == -1:
                    guard_see = False
                elif guard_see:
                    grid[r][c] = 2
        
        for c in range(n-1, -1, -1):
            guard_see = False
            for r in range(m-1, -1, -1):
                if grid[r][c] == 1:
                    guard_see = True
                elif grid[r][c] == -1:
                    guard_see = False
                elif guard_see:
                    grid[r][c] = 2
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += 1
        
        return count