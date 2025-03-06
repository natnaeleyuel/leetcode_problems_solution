class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numsdict = defaultdict(int)
        dup = 0
        presum = 0
        for row in grid:
            for col in row:
                presum += col
                if numsdict[col] > 0:
                    dup = col
                numsdict[col] += 1
        n = len(grid)
        n = n ** 2
        presum -= dup
        totsum = (n * (n + 1)) // 2
        miss = totsum - presum
        return [dup, miss]


