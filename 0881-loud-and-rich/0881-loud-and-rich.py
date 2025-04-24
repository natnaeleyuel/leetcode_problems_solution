class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0] * n
        for x, y in richer:
            graph[x].append(y)
            in_degree[y] += 1
        
        result = list(range(n))
        queue = deque()
        for node in range(n):
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            poped = queue.popleft()
            for nei in graph[poped]:
                if quiet[result[poped]] < quiet[result[nei]]:
                    result[nei] = result[poped]

                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return result