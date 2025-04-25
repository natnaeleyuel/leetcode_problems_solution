class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        color_dict = defaultdict(lambda: [float('inf'), float('inf'), -1, -1])
        n = len(targetGrid)
        m = len(targetGrid[0])
        for i in range(n):
            for j in range(m):
                color = targetGrid[i][j]
                color_dict[color][0] = min(color_dict[color][0], i)
                color_dict[color][1] = min(color_dict[color][1], j)
                color_dict[color][2] = max(color_dict[color][2], i)
                color_dict[color][3] = max(color_dict[color][3], j)

        graph = defaultdict(set)
        colors = list(color_dict.keys())

        for color in colors:
            x1, y1, x2, y2 = color_dict[color]
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    color2 = targetGrid[i][j]
                    if color2 != color:
                        graph[color2].add(color)
        
        visited = defaultdict(bool)
        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = True
            return True
        
        for color in colors:
            if color not in visited:
                if not dfs(color):
                    return False
        
        return True
