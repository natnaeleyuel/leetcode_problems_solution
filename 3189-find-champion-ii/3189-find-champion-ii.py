class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        called = defaultdict(int)
        for caller, callee in edges:
            called[callee] += 1
        
        res = 0
        freq = 0
        for callee in range(n):
            count = called[callee]
            if count == 0:
                if freq:
                    return -1
                freq += 1
                res = callee
        return res
        