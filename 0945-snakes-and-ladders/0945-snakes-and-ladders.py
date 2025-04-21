class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([1])
        visited = set()
        arr = [0] * (1 + n * n)  
        for i in range(n):
            for j in range(n):
                arr[(n - 1 - i) * n + (n - j if (n - i) % 2 == 0 else j + 1)] = board[i][j]
        res = 1
        while queue:
            for _ in range(len(queue)):
                poped = queue.popleft()
                for next in range(poped + 1, min(poped + 6, n * n) + 1):
                    dest = arr[next] if arr[next] > 0 else next
                    if dest == n * n:
                        return res
                    if dest in visited:
                        continue
                    queue.append(dest)
                    visited.add(dest)
            res += 1
        return -1