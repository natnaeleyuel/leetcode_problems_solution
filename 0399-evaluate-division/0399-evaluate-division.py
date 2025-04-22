class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))         
            graph[b].append((a, 1 / val))    

        def dfs(curr, tg, prod):
            if curr == tg:
                return prod
            visited.add(curr)
            for nei, wg in graph[curr]:
                if nei not in visited:
                    res = dfs(nei, tg, prod * wg)
                    if res != -1:
                        return res
            return -1

        results = []
        for i, j in queries:
            if i not in graph or j not in graph:
                results.append(-1.0)
            else:
                visited = set()
                results.append(dfs(i, j, 1.0))

        return [round(r, 5) for r in results]