class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1

        graph = [defaultdict(list), defaultdict(list)]
        for u, v in redEdges:
            graph[RED][u].append(v)
        for u, v in blueEdges:
            graph[BLUE][u].append(v)

        result = [-1] * n
        visited = [[False] * n for _ in range(2)]  

        queue = deque()
        queue.append((0, 0, -1))  

        while queue:
            node, dist, prev_color = queue.popleft()

            if result[node] == -1:
                result[node] = dist

            for color in [RED, BLUE]:
                if color == prev_color:
                    continue  
                for nei in graph[color][node]:
                    if not visited[color][nei]:
                        visited[color][nei] = True
                        queue.append((nei, dist + 1, color))

        return result