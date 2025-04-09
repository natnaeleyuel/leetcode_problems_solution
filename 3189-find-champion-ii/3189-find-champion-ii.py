class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        called = defaultdict(int)
        for caller, callie in edges:
            called[callie] += 1
        
        min_count = float('inf')
        res = 0
        freq = 0
        for callie in range(n):
            count = called[callie]
            if count == 0:
                if freq:
                    return -1
                # min_count = count
                freq += 1
                res = callie
        return res
        