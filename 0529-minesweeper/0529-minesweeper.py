class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        rows = len(board)
        cols = len(board[0])
        len(board[0])
        r, c = click
        
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def counter(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count

        def helper(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            mines = counter(r, c)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    helper(r + dr, c + dc)

        helper(r, c)
        return board