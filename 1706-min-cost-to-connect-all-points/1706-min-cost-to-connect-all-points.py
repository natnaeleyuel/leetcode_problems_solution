def md(a: List[int], b: List[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class DisjointUnion:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [0] * n
        
    def f(self, u):
        if self.p[u] != u:
            self.p[u] = self.f(self.p[u])

        return self.p[u]
    
    def u(self, u, v):
        u, v = self.f(u), self.f(v)

        if u == v:
            return False
            
        if self.r[u] > self.r[v]:
            u, v = v, u
        self.p[u] = v

        if self.r[u] == self.r[v]:
            self.r[v] += 1

        return True

class Solution:
    def minCostConnectPoints(self, pts: List[List[int]]) -> int:
        n = len(pts)
        dsu = DisjointUnion(n)
        heap = []
        
        for i in range(n):
            for j in range(i+1, n):
                heappush(heap, (md(pts[i], pts[j]), i, j))
        
        res = 0
        cnt = 0
        
        while heap:
            w, u, v = heappop(heap)
            if dsu.u(u, v):
                res += w
                cnt += 1
                if cnt == n - 1:
                    break
                    
        return res