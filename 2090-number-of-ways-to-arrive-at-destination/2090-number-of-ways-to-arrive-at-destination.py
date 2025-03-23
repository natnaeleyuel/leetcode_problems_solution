class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        mintime = [float('inf')] * n
        mintime[0] = 0  
        heap = [(0, 0)]  
        
        while heap:
            currtime, u = heapq.heappop(heap)
            if u == n - 1:
                break  
            if currtime > mintime[u]:
                continue  
            for v, time in graph[u]:
                if currtime + time < mintime[v]:
                    mintime[v] = currtime + time
                    heapq.heappush(heap, (mintime[v], v))
        
        if mintime[n - 1] == float('inf'):
            return 0
        
        dp = [0] * n
        dp[0] = 1  
        for u in sorted(range(n), key=lambda x: mintime[x]):
            for v, time in graph[u]:
                if mintime[u] + time == mintime[v]:
                    dp[v] = (dp[v] + dp[u]) % (10**9 + 7)
        
        return dp[n - 1]