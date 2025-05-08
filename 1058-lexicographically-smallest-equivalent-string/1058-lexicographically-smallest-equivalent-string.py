class DisjointUnion:
    def __init__(self, size):
        self.root = {}

    def find(self, x):
        self.root.setdefault(x, x)
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx > rooty:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        dsu = DisjointUnion(n)
        result = []

        for i in range(n):
            dsu.union(s1[i], s2[i])

        for c in baseStr:
            result.append(dsu.find(c))
        
        return ''.join(result)