class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        r, c = len(moveTime), len(moveTime[0])
        min_time = [[float('inf')] * c for _ in range(r)]
        pq = []
        heapq.heappush(pq, (-1, 0, 0, 1))
        min_time[0][0] = 0

        def update(i, j, steps, move):
            nextStep = move + max(steps, moveTime[i][j])
            if min_time[i][j] > nextStep:
                heapq.heappush(pq, (nextStep, i, j, 2 if move == 1 else 1))
                min_time[i][j] = nextStep

        while pq:
            steps, i, j, move = heapq.heappop(pq)

            if i + 1 < r: update(i + 1, j, steps, move)
            if i - 1 >= 0: update(i - 1, j, steps, move)
            if j + 1 < c: update(i, j + 1, steps, move)
            if j - 1 >= 0: update(i, j - 1, steps, move)

            if min_time[r - 1][c - 1] != float('inf'):
                return min_time[r - 1][c - 1]

        return -1