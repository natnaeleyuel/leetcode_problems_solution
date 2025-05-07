class DisjointUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.remain = size

    def get(self, a):
        if a == self.root[a]:
            return a

        self.root[a] = self.get(self.root[a])
        
        return self.root[a]

    def union(self, a, b):
        roota = self.get(a)
        rootb = self.get(b)
        if roota == rootb:
            return

        self.remain -= 1
        self.root[roota] = rootb 

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DisjointUnion(n)

        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dsu.union(i, j)
        
        result = n - dsu.remain
        return result


        