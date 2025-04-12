class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node2].append(node1)
        
        memo = defaultdict(int)
        def dfs(node):
            if node in memo:
                return memo[node]

            ance_set = set()
            for ance in graph[node]:
                ance_set.add(ance)
                ance_set.update(dfs(ance))
            memo[node] = ance_set
            return ance_set

        result = []
        for i in range(n):
            ance_set = dfs(i)
            result.append(sorted(ance_set))
        
        return result
        


        
