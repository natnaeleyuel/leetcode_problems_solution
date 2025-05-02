class UnionFind:
    def __init__(self, size):
        self.root = {i:i for i in range(size)}
        self.rank = {i:0 for i in range(size)}
        self.provinces = size
        
    def find(self, x):
        
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
		
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            rank1 = self.rank[rootx]
            rank2 = self.rank[rooty]
            
            if rank1 > rank2:
                self.root[rooty] = rootx
            elif rank2 > rank1:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.provinces -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)

        for city1 in range(n):
            for city2 in range(city1 + 1, n):
                if isConnected[city1][city2]:
                    dsu.union(city1, city2)
        
        return dsu.provinces

        

        