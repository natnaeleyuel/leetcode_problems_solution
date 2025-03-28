from queue import PriorityQueue
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rc = len(grid)
        cc = len(grid[0])
        result = [0] * len(queries)
        queries = sorted((val, ind) for ind, val in enumerate(queries))
        visited = [[False] * cc for _ in range(rc)]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        heap = PriorityQueue()
        heap.put((grid[0][0], 0, 0))
        visited[0][0] = True
        total = 0

        for val, ind in queries:
            while not heap.empty() and heap.queue[0][0] < val:
                currv, currr, currc = heap.get()
                total += 1

                for dr, dc in direction:
                    nr = currr + dr
                    nc = currc + dc

                    if nr >= 0 and nc >= 0 and nr < rc and nc < cc and not visited[nr][nc]:
                        heap.put((grid[nr][nc], nr, nc))
                        visited[nr][nc] = True
            result[ind] = total
        return result

