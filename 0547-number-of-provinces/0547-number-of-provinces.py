class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    connected[i + 1].append(j + 1)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in connected[node]:
                if neigh not in visited:
                    dfs(neigh)
            return 1
        
        res = 0
        for node in range(1, n + 1):
            if node not in visited:
                res += dfs(node)
        return res