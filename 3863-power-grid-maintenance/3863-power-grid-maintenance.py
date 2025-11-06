class DisjointUnion:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.active = [True] * (size + 1)
        self.heap = {i: [i] for i in range(size + 1)}

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        
        if rx < ry:
            self.root[ry] = rx
            for node in self.heap[ry]:
                heapq.heappush(self.heap[rx], node)
            del self.heap[ry]
        else:
            self.root[rx] = ry
            for node in self.heap[rx]:
                heapq.heappush(self.heap[ry], node)
            del self.heap[rx]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DisjointUnion(c)
        res = []

        for u, v in connections:
            dsu.union(u, v)

        for req, station in queries:
            if req == 1:
                root = dsu.find(station)
                heap = dsu.heap[root]

                while heap and not dsu.active[heap[0]]:
                    heapq.heappop(heap)
                
                if not dsu.active[station] and not heap:
                    res.append(-1)
                elif dsu.active[station]:
                    res.append(station)
                elif heap:
                    res.append(heap[0])
                else:
                    res.append(-1)

            else: 
                dsu.active[station] = False
        
        return res
