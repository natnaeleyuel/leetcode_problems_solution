class DisjointUnion:
    def __init__(self, size):
        self.rank = [1] * size 
        self.root = [i for i in range(size)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x]  = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            rankx = self.rank[rootx]
            ranky = self.rank[rooty]
            if rankx >= ranky:
                self.root[rooty] = rootx
                self.rank[rootx] += self.rank[rooty]
            elif rankx < ranky:
                self.root[rootx] = rooty
                self.rank[rooty] += self.rank[rootx]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DisjointUnion(n)
        result = [False] * len(queries)
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        
        ind = 0
        for w, p, q, i in queries:
            while ind < len(edgeList) and edgeList[ind][0] < w:
                dsu.union(edgeList[ind][1], edgeList[ind][2])
                ind += 1
            isValid = (dsu.find(p) == dsu.find(q))
            result[i] = isValid
        
        return result