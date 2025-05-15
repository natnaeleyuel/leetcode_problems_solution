class DisjointUnion:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.components = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.root[rootx] = rooty
            self.components -= 1
            return 1
        return 0
    
    def all_connected(self):
        return self.components == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        bob_dsu = DisjointUnion(n)
        alice_dsu = DisjointUnion(n)

        ind1 = 0
        ind2 = len(edges) - 1
        while ind1 < ind2:
            if edges[ind1][0] == 3:
                ind1 += 1
                continue 
            edges[ind1], edges[ind2] = edges[ind2], edges[ind1]
            ind2 -= 1

        redundant = 0
        for t, n1, n2 in edges:
            if t == 1:
                redundant += alice_dsu.union(n1, n2)
            elif t == 2:
                redundant += bob_dsu.union(n1, n2)
            else:
                redundant += alice_dsu.union(n1, n2) | bob_dsu.union(n1, n2)

            if bob_dsu.all_connected() and alice_dsu.all_connected():
                return len(edges) - redundant 

        if not bob_dsu.all_connected() or not alice_dsu.all_connected():
            return -1
        
        return len(edges) - redundant 

        


