class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # connected = defaultdict(list)
        # n = len(isConnected)
        # for i in range(n):
        #     for j in range(n):
        #         if i != j and isConnected[i][j] == 1:
        #             connected[i + 1].append(j + 1)
        
        # visited = set()
        # def dfs(node):
        #     visited.add(node)
        #     for neigh in connected[node]:
        #         if neigh not in visited:
        #             dfs(neigh)
        #     return 1
        
        # res = 0
        # for node in range(1, n + 1):
        #     if node not in visited:
        #         res += dfs(node)
        # return res

        connected = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    connected[i + 1].append(j + 1)
        root = defaultdict(int)
        def solve(node):
            root[node] = 1
            for nei in connected[node]:
                if root[nei] == 0:
                    solve(nei)
            return 1

        provinces = 0
        for node in range(1, n + 1):
            if root[node] == 0:
                provinces += solve(node)
        
        return provinces
        