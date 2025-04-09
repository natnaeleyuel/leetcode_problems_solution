class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = set()
        inbound = lambda x, y: x < n - 1 and x > 0 and y > 0 and y < m - 1
        direction = [(1, 0), (0, 1), (0, - 1), (-1, 0)]
        
        def helper(row, col):
            found = 0
            for i in range(0, col):
                if board[row][i] == 'X':
                    found += 1

            if found == 0:
                return False
            
            found = 0
            for i in range(col + 1, m):
                if board[row][i] == 'X':
                    found += 1

            if found == 0:
                return False

            found = 0
            for i in range(0, row):
                if board[i][col] == 'X':
                    found += 1

            if found == 0:
                return False
            
            found = 0
            for i in range(row + 1, n):
                if board[i][col] == 'X':
                    found += 1

            if found == 0:
                return False

            return True

        res = [True]
        def dfs(row, col):
            visited.add((row, col))
            ind = []
            if inbound(row, col) and helper(row, col):
                ind = [(row, col)]
            
            if not helper(row, col):
                res[0] = False

            for r, c in direction:
                new_row = row + r
                new_col = col + c
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == 'O':
                    ind += dfs(new_row, new_col)
                
            return ind
        
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and board[i][j] == 'O':
                    res[0] = True
                    ind = dfs(i, j)
                    if res[0]:
                        for row, col in ind:
                            board[row][col] = 'X'
            


        