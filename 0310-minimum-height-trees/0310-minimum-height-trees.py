class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        in_degree = [0] * n
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            in_degree[n1] += 1
            in_degree[n2] += 1

        queue = deque([])
        for node in range(n):
            if in_degree[node] == 1:
                queue.append(node)
        
        rd = n
        while rd > 2:
            rd -= len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        queue.append(nei)

        return list(queue)

