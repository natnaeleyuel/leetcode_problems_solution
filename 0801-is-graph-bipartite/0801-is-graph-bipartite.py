class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ug = -1
        gr = 1
        n = len(graph)
        colors_list = [ug] * n 

        def dfs(node, color):
            nonlocal result
            if not result:
                return 

            colors_list[node] = color
            for nei in graph[node]:
                if colors_list[nei] == ug:
                    dfs(nei, color ^ gr)
                elif colors_list[node] == colors_list[nei]:
                    result = False
                    
        result = True
        for node in range(n):
            if not result:
                return result
            if colors_list[node] == ug:
                dfs(node, 0)
                
        return result
