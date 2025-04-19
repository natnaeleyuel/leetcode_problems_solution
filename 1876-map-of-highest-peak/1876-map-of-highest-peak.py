class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        answer = [[-1] * m for _ in range(n)]
        queue = deque()
        
        for i, row in enumerate(isWater):
            for j, v in enumerate(row):
                if v == 1:  
                    queue.append((i, j))
                    answer[i][j] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        while queue:
            i, j = queue.popleft()
            for row, col in directions:
                new_row = i + row
                new_col = j + col
                if 0 <= new_row < n and 0 <= new_col < m and answer[new_row][new_col] == -1:
                    answer[new_row][new_col] = answer[i][j] + 1
                    queue.append((new_row, new_col))
        
        return answer
