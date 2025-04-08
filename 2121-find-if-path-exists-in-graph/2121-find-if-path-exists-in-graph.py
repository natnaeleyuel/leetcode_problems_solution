class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(graph, start, target):
            queue = deque([start])
            visited = set()
            while queue:
                node = queue.popleft()
                visited.add(node)
                if node == target:
                    return True
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        
            return False

        
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        return dfs(graph, source, destination)
        

