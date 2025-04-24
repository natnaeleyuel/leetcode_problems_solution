class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0] * n
        def dfs(node):
            if colors[node]:
                return colors[node] == 2
            colors[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            colors[node] = 2
            return True
        
        result = []
        for node in range(n):
            if dfs(node):
                result.append(node)
        
        return result