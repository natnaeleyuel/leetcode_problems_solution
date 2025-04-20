class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (n + 1) 
        
        for i in range(1, n + 1):
            if color[i] == 0:
                queue = deque([i])
                color[i] = 1
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == 0:
                            color[neighbor] = color[node] + 1
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True