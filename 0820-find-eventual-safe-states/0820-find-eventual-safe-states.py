class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        in_order = [len(graph[i]) for i in range(n)]
        g2 = defaultdict(list)
        for node in range(n):
            for nei in graph[node]:
                g2[nei].append(node)

        queue = deque([i for i in range(n) if len(graph[i]) == 0])
        result = []
        visited = set()
        while queue:
            curr = queue.popleft()
            result.append(curr)
            visited.add(curr)
            for anc in g2[curr]:
                in_order[anc] -= 1
                if anc not in visited and in_order[anc] == 0:
                    queue.append(anc)
        
        result.sort()
        return result